---
description: The read file content is corrupted by a leading space added to each line.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        nl -bn -w1 -s '' $LFILE
  suid:
    - code: |
        LFILE=file_to_read
        ./nl -bn -w1 -s '' $LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        sudo nl -bn -w1 -s '' $LFILE
---
