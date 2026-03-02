from .error import LinterError

from pathlib import Path
import schema
import yaml


def _string(x):
    if isinstance(x, str) and x == x.strip() and len(x) > 0:
        return True
    else:
        raise schema.SchemaError(f'{x!r} should be a non-empty space-trimmed string')


def _check_code_coherence(example):
    has_code = bool(example.get('code'))
    all_contexts_have_code = all(
        context and context.get('code')
        for context in example.get('contexts', {}).values()
    )
    if has_code != all_contexts_have_code:
        return True
    else:
        raise schema.SchemaError(f'{example!r} should provide the code')


def _context(name, per_context_schema):
    return {
        schema.Optional(name): schema.Or(None, {
            schema.Optional('code'): _string,
            schema.Optional('comment'): _string,
            **per_context_schema,
        })
    }


def _gtfobin(name):
    if name in _gtfobins:
        return True
    else:
        raise schema.SchemaError(f'{name!r} does not exist')


def _function(name, per_function_schema):
    return {
        schema.Optional(name): schema.And(len, [
            schema.And({
                schema.Optional('code'): _string,
                schema.Optional('comment'): _string,
                schema.Optional('version'): schema.Or(_string, int, float),
                schema.Optional('mitre'): [
                    schema.Regex(r'^T[0-9]+$'),
                ],
                **per_function_schema,
                'contexts': {
                    **_context('unprivileged', {
                    }),
                    **_context('sudo', {
                    }),
                    **_context('suid', {
                        schema.Optional('shell'): bool,
                    }),
                    **_context('capabilities', {
                        schema.Optional('list'): schema.And(len, [
                            schema.Regex(r'^CAP_[A-Z_]+$'),
                        ]),
                    }),
                }
            }, _check_code_coherence),
        ]),
    }


_root = Path(__file__).parent / '..'
_functions = yaml.safe_load((_root / '_data' / 'functions.yml').read_text());
_gtfobins = {file.name for file in (_root / '_gtfobins').iterdir()}


_additional_example = {
    schema.Or('code', 'comment'): _string,
}


_binary = {
    schema.Optional('binary'): bool,
}


_blind = {
    schema.Optional('blind'): bool,
}


_tty = {
    schema.Optional('tty'): bool,
}


_listener = {
    schema.Optional('listener'): schema.Or(
        _additional_example,
        *_functions['reverse-shell']['extra']['listener'].keys(),
    )
}


_connector = {
    schema.Optional('connector'): schema.Or(
        _additional_example,
        *_functions['bind-shell']['extra']['connector'].keys(),
    )
}


_receiver = {
    schema.Optional('receiver'): schema.Or(
        _additional_example,
        *_functions['upload']['extra']['receiver'].keys(),
    )
}


_sender = {
    schema.Optional('sender'): schema.Or(
        _additional_example,
        *_functions['download']['extra']['sender'].keys(),
    )
}


_SCHEMA = schema.Or(
    {
        'alias': _string,
    },
    {
        schema.Optional('comment'): _string,
        'functions': schema.And(len, {
            **_function('shell', {
                **_tty,
                **_blind,
            }),
            **_function('command', {
                **_blind,
            }),
            **_function('reverse-shell', {
                **_tty,
                **_blind,
                **_listener,
            }),
            **_function('bind-shell', {
                **_tty,
                **_blind,
                **_connector,
            }),
            **_function('file-write', {
                **_binary,
            }),
            **_function('file-read', {
                **_binary,
            }),
            **_function('upload', {
                **_binary,
                **_receiver,
            }),
            **_function('download', {
                **_binary,
                **_sender,
            }),
            **_function('library-load', {
            }),
            **_function('privilege-escalation', {
            }),
            **_function('inherit', {
                'from': _gtfobin,
            }),
        }),
    }
)

def validate(data):
    try:
        _SCHEMA.validate(data)
    except schema.SchemaError as e:
        raise LinterError(str(e.autos[-1]))
