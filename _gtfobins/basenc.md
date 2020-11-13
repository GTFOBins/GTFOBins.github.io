---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        basenc --base16 $LFILE | basenc -d --base16
  suid:
    - code: |
        LFILE=file_to_read
        basenc --base16 $LFILE | basenc -d --base16
  sudo:
    - code: |
        LFILE=file_to_read
        sudo basenc --base16 $LFILE | basenc -d --base16
---
