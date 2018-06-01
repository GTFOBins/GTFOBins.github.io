---
description: |
  The read file content is corrupted by a leading space added to each line.
functions:
  sudo-enabled:
    - code: |
        LFILE=file_to_read
        sudo nl -bn -w1 -s '' $LFILE
  suid-enabled:
    - code: |
        LFILE=file_to_read
        ./nl -bn -w1 -s '' $LFILE
  file-read:
    - code: |
        LFILE=file_to_read
        nl -bn -w1 -s '' $LFILE
---
