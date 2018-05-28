---
functions:
  file-read:
    - code: dd if=file_to_read
  file-write:
    - code: echo "data" | dd of=file_to_write
---
