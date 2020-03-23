---
description: Make sure that `RANDOM` does not appear into the file to read otherwise the content of the file is corrupted by reversing the order of `RANDOM`-separated chunks.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        tac -s 'RANDOM' "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./tac -s 'RANDOM' "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo tac -s 'RANDOM' "$LFILE"
---
