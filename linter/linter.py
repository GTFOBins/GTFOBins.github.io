from . import schema

from schema import SchemaError

import yaml
import yamllint.config
import yamllint.linter


_YAML_LINT_CONFIG = '''
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


def lint(path):
    with open(path) as fs:
        # attempt YAML parsing
        try:
            text = fs.read()
            data = yaml.safe_load(text)
        except yaml.YAMLError as e:
            return [f'{e.problem} at line {e.problem_mark.line}']

        problems = []

        # check YAML syntax
        config = yamllint.config.YamlLintConfig(_YAML_LINT_CONFIG)
        for problem in yamllint.linter.run(text, config):
            problems.append(f'{problem.desc} at line {problem.line}')

        # check valid schema
        try:
            schema.validate(data)
        except SchemaError as e:
            problems.append(str(e.autos[-1]))

        return problems
