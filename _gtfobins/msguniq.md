---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        /usr/bin/msguniq -P "${LFILE}"
  sudo:
    - code: |
        LFILE=file_to_read
        /usr/bin/msguniq -P "${LFILE}"
  suid:
    - code: |
        LFILE=file_to_read
        /usr/bin/msguniq -P "${LFILE}"
---
