from . import linter

import argparse
import os
import re
import sys


def report_fail(name, error):
    print(f'\x1b[31;1mFAIL\x1b[0m {name}')
    print(f'   - {error}')


def report_pass(name):
    print(f'\x1b[32;1mPASS\x1b[0m {name}')


def run(check_only, verbose):
    # move into the GTFOBins directory
    os.chdir('_gtfobins')

    # process all the entries
    for name in sorted(os.listdir()):
        # check for old-version files
        if re.search(r'\.(md|yaml|yml)$', name):
            report_fail(name, 'entries must have no extension')
            return False

        # check linter errors
        if error := linter.lint(name, check_only):
            report_fail(name, error)
            return False

        # otherwise pass
        if verbose:
            report_pass(name)

    return True


def main():
    # parse argumenst
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--check-only', action='store_true')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()

    # start!
    sys.exit(not run(**vars(args)))


main()
