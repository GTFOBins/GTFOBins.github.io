---
description: The output is placed inside the ISO9660 file system binary format thus it may not be suitable for binary content.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        genisoimage -q -o - "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo genisoimage -q -o - "$LFILE"
---
