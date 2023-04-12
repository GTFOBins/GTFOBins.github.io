---
functions:
  file-write:  # should be file-copy
    - code: |
        LFILE1=file_to_read
        LFILE2=file_to_write
        dos2unix -f -n "$LFILE1" "$LFILE2"
---
