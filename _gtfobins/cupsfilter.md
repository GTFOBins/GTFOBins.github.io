---
description: |
    cupsfilter - convert a file to another format using cups filters (deprecated).
    By default, it converts the file into a PDF ( default output mime: application/pdf ).
    Available options:
        -i "mime/type"  # input mime/type
        -m "mime/type"  # output mime/type
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        cupsfilter $LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        sudo cupsfilter $LFILE
  suid:
    - code: |
        LFILE=file_to_read
        ./cupsfilter $LFILE
---
