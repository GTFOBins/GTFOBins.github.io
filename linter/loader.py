from .error import LinterError

import yaml


def load(path):
    # try to load the YAML file reporting parsing errors
    try:
        with open(path, 'r') as fs:
            text = fs.read()
            data = yaml.safe_load(text)
            return text, data
    except yaml.YAMLError as e:
        raise LinterError(f'{e.problem} at line {e.problem_mark.line}')
