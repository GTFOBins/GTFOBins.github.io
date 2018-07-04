---
functions:
  file-write:
  - code: |
      LFILE=file_to_write
      echo "data" | dd of=$LFILE
  file-read:
  - code: |
      LFILE=file_to_read
      dd if=LFILE
---
