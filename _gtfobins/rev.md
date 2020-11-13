---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        rev $LFILE | rev
  suid:
    - code: |
        LFILE=file_to_read
        ./rev $LFILE | rev
  sudo:
    - code: |
        LFILE=file_to_read
        sudo rev $LFILE | rev
---
