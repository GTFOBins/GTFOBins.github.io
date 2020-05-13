#!/usr/bin/env python3
import jsonschema
import os
import sys
import yaml

def parse_yaml(path):
    with open(path) as fs:
        text = fs.read()
        return yaml.load_all(text, Loader=yaml.SafeLoader)

def build_schema():
    function_names = next(parse_yaml('_data/functions.yml')).keys()
    return {
        "definitions": {
            'examples': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'description': {'type': 'string'},
                        'code': {'type': 'string'}
                    },
                    'required': ['code'],
                    'additionalProperties': False
                },
                'minimum': 1
            }
        },
        'type': 'object',
        'properties': {
            'description': {'type': 'string'},
            'functions': {
                'type': 'object',
                "patternProperties": {
                    '^({})$'.format('|'.join(function_names)): {'$ref': '#/definitions/examples'}
                },
                'additionalProperties': False
            }
        },
        'required': ['functions'],
        'additionalProperties': False
    }

def validate_directory(root):
    schema = build_schema()
    root, _, files = next(os.walk(root))
    for name in files:
        if not name.endswith('.md'):
            continue
        path = os.path.join(root, name)
        data = parse_yaml(path)
        try:
            jsonschema.validate(next(data), schema)
        except jsonschema.exceptions.ValidationError as err:
            print('{}: {}'.format(name, err))
            sys.exit(1)

if __name__ == '__main__':
    validate_directory("_gtfobins/")
