---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        /usr/bin/msgfilter -P -i "${LFILE}" [cat, sed "", tac, <filter-name>]
  sudo:
    - code: |
        LFILE=file_to_read
        /usr/bin/msgfilter -P -i "${LFILE}" [cat, sed "", tac, <filter-name>]
  suid:
    - code: |
        LFILE=file_to_read
        /usr/bin/msgfilter -P -i "${LFILE}" [cat, sed "", tac, <filter-name>]
---
