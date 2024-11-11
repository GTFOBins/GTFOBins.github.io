---
functions:
  sudo:
    - code: |
        LFILE=file_to_read
        sudo mutt -F $LFILE
    - code: |
        LFILE=file_to_read
        sudo mutt -i $LFILE
---
