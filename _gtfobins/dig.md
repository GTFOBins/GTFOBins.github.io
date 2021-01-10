---
functions:
  file-read:
    - description: Each input line is treated as a lookup query for `dig` command and the output is corrupted with the result or errors of the operation, so this may not be suitable for binary files.
      code: |
        LFILE=file_to_read
        dig -f $LFILE
  sudo:
    - description: Each input line is treated as a lookup query for `dig` command and the output is corrupted with the result or errors of the operation, so this may not be suitable for binary files.
      code: |
        LFILE=file_to_read
        sudo dig -f $LFILE

---
