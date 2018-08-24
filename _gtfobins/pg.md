---
functions:
  execute-interactive:
    - code: |
        pg /etc/profile
        !/bin/sh
  file-read:
    - code: pg file_to_read
  sudo-enabled:
    - code: |
        sudo pg /etc/profile
        !/bin/sh
  suid-enabled:
    - code: ./pg file_to_read
---
