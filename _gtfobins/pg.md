---
functions:
  shell:
    - code: |
        pg /etc/profile
        !/bin/sh
  file-read:
    - code: pg file_to_read
  sudo:
    - code: |
        sudo pg /etc/profile
        !/bin/sh
  suid:
    - code: ./pg file_to_read
---
