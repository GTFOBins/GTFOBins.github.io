#!/usr/bin/env python3

import os
import schema
import sys
import yaml
import yamllint.config
import yamllint.linter


YAML_LINT_CONFIG = '''
extends: default
rules:
  line-length: disable
  document-start:
    present: true
  document-end:
    present: true
  indentation:
    spaces: 2
    check-multi-line-strings: true
  brackets:
    forbid: true
  braces:
    forbid: true
'''

LAX = os.environ.get('MODE') == 'lax'


class Linter():

    def __init__(self):
        self._config = yamllint.config.YamlLintConfig(YAML_LINT_CONFIG)
        self._schema = self._build_schema()

    def _build_schema(self):
        def string(x):
            if isinstance(x, str) and x == x.strip() and len(x) > 0:
                return True
            else:
                raise schema.SchemaError(f'{x!r} should be a non-empty space-trimmed string')

        def check_code_coherence(example):
            has_code = bool(example.get('code'))
            has_contexts = bool(example.get('contexts'))
            all_contexts_have_code = all(
                context and context.get('code')
                for context in example.get('contexts', {}).values()
            )
            if has_code != (has_contexts and all_contexts_have_code):
                return True
            else:
                raise schema.SchemaError(f'{example!r} should provide the code')

        def context(name, per_context_schema):
            return {
                schema.Optional(name): schema.Or(None, {
                    schema.Optional('code'): string,
                    schema.Optional('comment'): string,
                    **per_context_schema,
                })
            }

        def function(name, per_function_schema):
            return {
                schema.Optional(name): schema.And(len, [
                    schema.And({
                        schema.Optional('code'): string,
                        schema.Optional('comment'): string,
                        schema.Optional('version'): string,
                        schema.Optional('mitre'): string,
                        **per_function_schema,
                        schema.Optional('contexts'): {
                            **context('unprivileged', {
                            }),
                            **context('sudo', {
                            }),
                            **context('suid', {
                                schema.Optional('shell'): bool,
                            }),
                            **context('capabilities', {
                                schema.Optional('list'): schema.And(len, [
                                    schema.Regex(r'^CAP_[A-Z_]+$'),
                                ]),
                            }),
                        }
                    }, check_code_coherence),
                ]),
            }

        network_protocols = schema.Or(
            {
                schema.Or('code', 'comment'): string,
            },
            # TODO actually fetch known protocols from data files?
            'HTTP',
            # ...
        )

        binary = {
            schema.Optional('binary'): bool,
        }

        blind = {
            schema.Optional('blind'): bool,
        }

        tty = {
            schema.Optional('tty'): bool,
        }

        return schema.Or(
            {
                'alias': string,
            },
            {
                schema.Optional('comment'): string,
                'functions': schema.And(len, {
                    **function('shell', {
                        **blind,
                    }),
                    **function('command', {
                        **blind,
                    }),
                    **function('reverse-shell', {
                        **tty,
                        **blind,
                        schema.Optional('listener'): network_protocols,
                    }),
                    **function('bind-shell', {
                        **tty,
                        **blind,
                        schema.Optional('connector'): network_protocols,
                    }),
                    **function('file-write', {
                        **binary,
                    }),
                    **function('file-read', {
                        **binary,
                    }),
                    **function('upload', {
                        **binary,
                        schema.Optional('receiver'): network_protocols,
                    }),
                    **function('download', {
                        **binary,
                        schema.Optional('sender'): network_protocols,
                    }),
                    **function('library-load', {
                    }),
                    **function('inherit', {
                        'from': string,
                    }),
                }),
            }
        )

    def lint(self, path):
        with open(path) as fs:
            # attempt YAML parsing
            try:
                text = fs.read()
                data = yaml.safe_load(text)
            except yaml.YAMLError as e:
                return [f'{e.problem} at line {e.problem_mark.line}']

            problems = []

            # check YAML syntax
            for problem in yamllint.linter.run(text, self._config):
                problems.append(f'{problem.desc} at line {problem.line}')

            # check valid schema
            try:
                self._schema.validate(data)
            except schema.SchemaError as e:
                problems.append(str(e.autos[-1]))

            return problems


def run():
    success = True

    # move into the GTFOBins directory
    os.chdir('_gtfobins')

    # lint all the entries
    linter = Linter()
    for name in sorted(os.listdir()):
        # skip old-version files
        if name.endswith('.md'):
            print(f'\x1b[33;1mTODO\x1b[0m {name}')
            if LAX:
                continue
            else:
                return False

        # lint and report the outcome
        problems = linter.lint(name)
        if problems:
            success = False
            print(f'\x1b[31;1mFAIL\x1b[0m {name}')
            for problem in problems:
                print(f'     - {problem}')
            if not LAX:
                return False
        else:
            print(f'\x1b[32;1mPASS\x1b[0m {name}')

    return success


if __name__ == '__main__':
    sys.exit(not run())
