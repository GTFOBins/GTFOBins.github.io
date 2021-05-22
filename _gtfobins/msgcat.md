---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        /usr/bin/msgcat -P "${LFILE}"
  sudo:
    - code: |
        LFILE=file_to_read
        /usr/bin/msgcat -P "${LFILE}"
  suid:
    - code: |
        LFILE=file_to_read
        /usr/bin/msgcat -P "${LFILE}"
---
