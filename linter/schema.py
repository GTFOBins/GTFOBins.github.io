from .error import LinterError

import schema


def _string(x):
    if isinstance(x, str) and x == x.strip() and len(x) > 0:
        return True
    else:
        raise schema.SchemaError(f'{x!r} should be a non-empty space-trimmed string')


def _check_code_coherence(example):
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


def _context(name, per_context_schema):
    return {
        schema.Optional(name): schema.Or(None, {
            schema.Optional('code'): _string,
            schema.Optional('comment'): _string,
            **per_context_schema,
        })
    }


def _function(name, per_function_schema):
    return {
        schema.Optional(name): schema.And(len, [
            schema.And({
                schema.Optional('code'): _string,
                schema.Optional('comment'): _string,
                schema.Optional('version'): _string,
                schema.Optional('mitre'): _string,
                **per_function_schema,
                schema.Optional('contexts'): {
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


_network_protocols = schema.Or(
    {
        schema.Or('code', 'comment'): _string,
    },
    # TODO actually fetch known protocols from data files?
    'HTTP',
    # ...
)


_binary = {
    schema.Optional('binary'): bool,
}


_blind = {
    schema.Optional('blind'): bool,
}


_tty = {
    schema.Optional('tty'): bool,
}

_SCHEMA = schema.Or(
    {
        'alias': _string,
    },
    {
        schema.Optional('comment'): _string,
        'functions': schema.And(len, {
            **_function('shell', {
                **_blind,
            }),
            **_function('command', {
                **_blind,
            }),
            **_function('reverse-shell', {
                **_tty,
                **_blind,
                schema.Optional('listener'): _network_protocols,
            }),
            **_function('bind-shell', {
                **_tty,
                **_blind,
                schema.Optional('connector'): _network_protocols,
            }),
            **_function('file-write', {
                **_binary,
            }),
            **_function('file-read', {
                **_binary,
            }),
            **_function('upload', {
                **_binary,
                schema.Optional('receiver'): _network_protocols,
            }),
            **_function('download', {
                **_binary,
                schema.Optional('sender'): _network_protocols,
            }),
            **_function('library-load', {
            }),
            **_function('inherit', {
                'from': _string,
            }),
        }),
    }
)

def validate(data):
    try:
        _SCHEMA.validate(data)
    except schema.SchemaError as e:
        raise LinterError(str(e.autos[-1]))
