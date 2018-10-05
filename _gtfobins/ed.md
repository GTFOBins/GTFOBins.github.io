---
functions:
  shell:
    - code: |
        ed
        !/bin/sh
  file-write:
    - code: |
        ed file_to_write
        a
        DATA
        .
        w
        q
  file-read:
    - code: |
        ed file_to_read
        ,p
        q
  sudo:
    - code: |
        sudo ed
        !/bin/sh
  limited-suid:
    - code: |
        ./ed
        !/bin/sh
---
