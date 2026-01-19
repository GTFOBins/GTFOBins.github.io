from .error import LinterError

import yaml


class _Dumper(yaml.SafeDumper):
    pass


# use pipe style for certain string fields


class _BlockString(str):
    pass


def _block_string_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')


_Dumper.add_representer(_BlockString, _block_string_representer)


def _ensure_block_style(o):
    match o:
        case dict():
            return {
                k: (_BlockString(v) if k in ('code', 'comment', 'version') else _ensure_block_style(v))
                for k, v in o.items()
            }

        case list():
            return [
                _ensure_block_style(v) for v in o
            ]

        case _:
            return o


# omit explicit null


def _none_representer(dumper, _):
    return dumper.represent_scalar('tag:yaml.org,2002:null', '')


_Dumper.add_representer(type(None), _none_representer)


###


def dump(text, data, path, check_only):
    # serialize the data object
    data = _ensure_block_style(data)
    formatted = yaml.dump(data, Dumper=_Dumper, explicit_start=True, explicit_end=True)

    # if not properly formatted
    if formatted != text:
        if check_only:
            # report error
            raise LinterError('schema OK but invalid format, please run the formatter')
        else:
            # write the formatted file
            with open(path, 'w') as fs:
                fs.write(formatted)
