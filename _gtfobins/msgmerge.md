---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        /usr/bin/msgmerge -P "${LFILE}" /dev/null
  sudo:
    - code: |
        LFILE=file_to_read
        /usr/bin/msgmerge -P "${LFILE}" /dev/null
  suid:
    - code: |
        LFILE=file_to_read
        /usr/bin/msgmerge -P "${LFILE}" /dev/null
---
