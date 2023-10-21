---
functions:
  shell:
    - description: |
        Start the following command to open the TUI interface, then:
        1. press `Ctrl-A o` and select `Filenames and paths`;
        2. press `E` and type `/bin/sh`;
        3. Press `Esc` twice;
        4. Press `Ctrl-A k` to drop the shell.
        After the shell, exit with `Ctrl-A x`. Note that in some versions, `Meta-Z` is used in place of `Ctrl-A`.
      code: |
        minicom -D /dev/null
---
