---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        basenc --base64 $LFILE | basenc -d --base64
  suid:
    - code: |
        LFILE=file_to_read
        basenc --base64 $LFILE | basenc -d --base64
  sudo:
    - code: |
        LFILE=file_to_read
        sudo basenc --base64 $LFILE | basenc -d --base64
---
