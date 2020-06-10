---
functions:
  shell:
    - code: |
        TERM= more /etc/profile
        !/bin/sh
  file-read:
    - code: more file_to_read
  suid:
    - code: ./more file_to_read
  sudo:
    - code: |
        TERM= sudo more /etc/profile
        !/bin/sh
---
