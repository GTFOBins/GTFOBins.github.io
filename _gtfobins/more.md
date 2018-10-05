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
        TERM= sudo -E more /etc/profile
        !/bin/sh
---
