---
description: Outputs the first line of the file to standard error without the `-` and `#` characters, this can be customized with the `-c` option, by default is `-c -#`.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        atobm $LFILE 2>&1 | awk -F "'" '{printf "%s", $2}'
  sudo:
    - code: |
        LFILE=file_to_read
        sudo atobm $LFILE 2>&1 | awk -F "'" '{printf "%s", $2}'
  suid:
    - code: |
        LFILE=file_to_read
        ./atobm $LFILE 2>&1 | awk -F "'" '{printf "%s", $2}'
---
