---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        /usr/bin/msgattrib -P "${LFILE}"
  sudo:
    - code: |
        LFILE=file_to_read
        /usr/bin/msgattrib -P "${LFILE}"
  suid:
    - code: |
        LFILE=file_to_read
        /usr/bin/msgattrib -P "${LFILE}"
---
