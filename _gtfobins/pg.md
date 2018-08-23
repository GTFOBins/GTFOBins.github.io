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
  suid-limited:
    - code: |
        ./pg /etc/profile
        !/bin/sh
---
