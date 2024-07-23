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


class Linter():

    def __init__(self):
        self._config = yamllint.config.YamlLintConfig(YAML_LINT_CONFIG)
        self._schema = self._build_schema()

    def _build_schema(self):
        non_empty_string = schema.And(str, len)

        default_context_example_fields = {
            schema.Optional('description'): non_empty_string,
            schema.Optional('code'): non_empty_string,
        }

        default_function_example_fields = {
            **default_context_example_fields,
            schema.Optional('version'): non_empty_string,
        }

        description_or_code = {
            schema.Or('description', 'code'): non_empty_string,
        }

        network_shell_counterpart = schema.Or(
            description_or_code,
            # ...
        )

        network_file_counterpart = schema.Or(
            description_or_code,
            # ...
        )

        def contexts(names, context_schema):
            return {
                schema.Optional(schema.Or(*names)): schema.Or(None, {
                    **default_context_example_fields,
                    **context_schema,
                })
            }

        contexts = {
            schema.Optional('contexts'): {
                **contexts(['unprivileged', 'sudo'], {}),
                **contexts(['suid'], {
                    schema.Optional('limited'): bool,
                }),
                **contexts(['capabilities'], {
                    schema.Optional('list'): schema.And(len, [
                        schema.Regex(r'^CAP_[A-Z_]+'),
                    ]),
                }),
            }
        }

        def functions(names, example_schema):
            def check_code_coherence(example):
                has_code = bool(example.get('code'))
                has_contexts = bool(example.get('contexts'))
                all_contexts_have_code = all(map(lambda x: x.get('code'), example.get('contexts', {}).values()))
                return has_code != (has_contexts and all_contexts_have_code)

            return {
                schema.Optional(schema.Or(*names)): schema.And(len, [
                    schema.And({
                        **default_function_example_fields,
                        **example_schema,
                        **contexts,
                    }, check_code_coherence),
                ]),
            }

        functions = {
            'functions': schema.And(len, {
                **functions(['shell', 'command', 'library-load'], {}),
                **functions(['reverse-shell'], {
                    schema.Optional('limited'): bool,
                    schema.Optional('listener'): network_shell_counterpart,
                }),
                **functions(['bind-shell'], {
                    schema.Optional('limited'): bool,
                    schema.Optional('connector'): network_shell_counterpart,
                }),
                **functions(['file-write'], {
                    schema.Optional('limited'): bool,
                }),
                **functions(['file-read'], {
                    schema.Optional('limited'): bool,
                }),
                **functions(['upload'], {
                    schema.Optional('limited'): bool,
                    schema.Optional('receiver'): network_file_counterpart,
                }),
                **functions(['download'], {
                    schema.Optional('limited'): bool,
                    schema.Optional('sender'): network_file_counterpart,
                }),
                **functions(['inherit'], {
                    'from': non_empty_string,
                }),
            }),
        }

        return schema.Schema(
            schema.Or({
                'alias': non_empty_string,
            }, {
                schema.Optional('description'): non_empty_string,
                **functions,
            })
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
            continue

        # lint and report the outcome
        problems = linter.lint(name)
        if problems:
            success = False
            print(f'\x1b[31;1mFAIL\x1b[0m {name}')
            for problem in problems:
                print(f'     - {problem}')
        else:
            print(f'\x1b[32;1mPASS\x1b[0m {name}')

    return success


if __name__ == '__main__':
    sys.exit(not run())
