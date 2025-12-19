from . import linter

import os
import sys


LAX = os.environ.get('MODE') == 'lax'


def run():
    success = True

    # move into the GTFOBins directory
    os.chdir('_gtfobins')

    # lint all the entries
    for name in sorted(os.listdir()):
        # skip old-version files
        if name.endswith('.md'):
            print(f'\x1b[33;1mTODO\x1b[0m {name}')
            if LAX:
                continue
            else:
                return False

        # lint and report the outcome
        problems = linter.lint(name)
        if problems:
            success = False
            print(f'\x1b[31;1mFAIL\x1b[0m {name}')
            for problem in problems:
                print(f'     - {problem}')
            if not LAX:
                return False
        else:
            print(f'\x1b[32;1mPASS\x1b[0m {name}')

    return success


sys.exit(not run())
