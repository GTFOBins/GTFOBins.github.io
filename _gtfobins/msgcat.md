---
description: The file is parsed and displayed as a Java `.properties` file, so this may not be suitable to read arbitrary binary data.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        msgcat -P $LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        sudo msgcat -P $LFILE
  suid:
    - code: |
        LFILE=file_to_read
        ./msgcat -P $LFILE
---
