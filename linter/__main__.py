from . import linter

import argparse
import os
import sys


def run(check_only):

    # move into the GTFOBins directory
    os.chdir('_gtfobins')

    # process all the entries
    for name in sorted(os.listdir()):
        # skip old-version files (TODO remove after migration)
        if name.endswith('.md'):
            print(f'\x1b[33;1mTODO\x1b[0m {name}')
            return False

        # lint and report the outcome
        if error := linter.lint(name, check_only):
            print(f'\x1b[31;1mFAIL\x1b[0m {name}')
            print(f'   - {error}')
            return False
        else:
            print(f'\x1b[32;1mPASS\x1b[0m {name}')

    return True


def main():
    # parse argumenst
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--check-only', action='store_true')
    args = parser.parse_args()

    # start!
    sys.exit(not run(args.check_only))


main()
