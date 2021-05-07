---
description: The file is displayed in a Xorg window, so it needs a working graphical environment.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        xmore $LFILE
  suid:
    - code: |
        LFILE=file_to_read
        ./xmore $LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        sudo xmore $LFILE
---
