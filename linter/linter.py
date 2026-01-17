from . import dumper
from . import loader
from . import schema
from .error import LinterError


def lint(path, check_only):
    try:
        # load the YAML file
        data = loader.load(path)

        # validate the content
        schema.validate(data)

        # save or check the formatted YAML file
        dumper.dump(data, path, check_only)
    except LinterError as e:
        return str(e)
