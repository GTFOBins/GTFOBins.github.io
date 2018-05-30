---
functions:
  file-read:
    - description: This prepends a leading space to each line.
      code: |
        LFILE=file_to_read
        nl -bn -w1 -s '' $LFILE
---
