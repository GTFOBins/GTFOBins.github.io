---
description: The file is parsed and displayed as a Java `.properties` file, so this may not be suitable to read arbitrary binary data.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        msgattrib -P $LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        sudo msgattrib -P $LFILE
  suid:
    - code: |
        LFILE=file_to_read
        ./msgattrib -P $LFILE
---
