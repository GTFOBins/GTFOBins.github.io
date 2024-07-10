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
'''


class Linter():

    def __init__(self):
        self._yaml_lint_config = yamllint.config.YamlLintConfig(YAML_LINT_CONFIG)
        self._schema = self._build_schema()

    def _load_yaml_file(path):
        with open(path) as fs:
            return yaml.safe_load(fs)

    def _build_schema(self):
        # fetch external data files
        functions = Linter._load_yaml_file('_data/functions.yml')
        contexts = Linter._load_yaml_file('_data/contexts.yml')

        # gather functions and contexts that does not have special properties
        simple_functions = set(functions.keys()) - {'inherit', 'reverse-shell', 'bind-shell'}
        simple_contexts = set(contexts.keys()) - {'suid', 'capabilities'}

        # common schema parts
        non_empty_string = schema.And(str, len)
        default_fields = {
            schema.Optional('description'): non_empty_string,
            schema.Optional('code'): non_empty_string
        }
        contexts = {
            schema.Optional('contexts'): {
                schema.Optional(schema.Or(*simple_contexts)): schema.Or(None, {
                    **default_fields
                }),
                # per-context properties...
                schema.Optional('suid'): schema.Or(None, {
                    **default_fields,
                    schema.Optional('limited'): bool
                }),
                schema.Optional('capabilities'): schema.Or(None, {
                    **default_fields,
                    schema.Optional('list'): [non_empty_string]
                }),
            }
        }

        return schema.Schema(
            schema.Or({
                'alias': non_empty_string
            }, {
                schema.Optional('description'): non_empty_string,
                'functions': {
                    schema.Optional(schema.Or(*simple_functions)): [schema.And(len, {
                        **default_fields,
                        **contexts
                    })],
                    schema.Optional(schema.Or('reverse-shell', 'bind-shell')): [schema.And(len, {
                        **default_fields,
                        schema.Optional('tty'): bool,
                        **contexts
                    })],
                    schema.Optional('inherit'): [schema.And(len, {
                        **default_fields,
                        'from': non_empty_string,
                        **contexts
                    })]
                }
            })
        )

    def _check_coherence(self, data):
        # make sure that every example has a code element when there is no fallback
        for function_name, function in data.get('functions', {}).items():
            for index, example in enumerate(function):
                contexts = example.get('contexts')
                code = example.get('code')
                if not code:
                    message = "Missing 'code' for '{}' function at example {}".format(function_name, index)
                    if contexts:
                        for context_name, context in contexts.items():
                            assert context and context.get('code'), message
                    else:
                        assert code, message


    def _lint_file(self, path):
        problems = []
        with open(path) as fs:
            # prepare the name for ANSI printing
            name = '\x1b[31;1m{}\x1b[0m'.format(os.path.basename(path))

            # attempt YAML parsing
            try:
                text = fs.read()
                data = yaml.safe_load(text)
            except yaml.YAMLError as e:
                problems.append('{}: {}'.format(name, e))
                return problems

            # check valid YAML syntax
            for problem in yamllint.linter.run(text, self._yaml_lint_config):
                problems.append('{}:{}: [{}] {}'.format(name, problem.line, problem.rule, problem.desc))

            # check valid schema
            try:
                self._schema.validate(data)
            except schema.SchemaError as e:
                problems.append('{}: {}'.format(name, e))

            # check additional coherence
            try:
                self._check_coherence(data)
            except AssertionError as e:
                problems.append('{}: {}'.format(name, e))

        return problems

    def run(self):
        root = '_gtfobins'
        success = True

        # walk and lint all the gtfobins
        for name in sorted(os.listdir(root)):
            # skip old version files
            if name.endswith('.md'):
                continue

            # lint and report errors
            path = os.path.join(root, name)
            for problem in self._lint_file(path):
                success = False
                print(problem)

        return success


if __name__ == '__main__':
    sys.exit(not Linter().run())
