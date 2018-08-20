---
functions:
  execute-interactive:
    - code: |
        ed
        !/bin/sh
  file-write:
    - code: |
        ed file_to_write
        a
        data
        .
        w
        q
  file-read:
    - code: |
        ed file_to_read
        ,p
        q
  sudo-enabled:
    - code: |
        sudo ed
        !/bin/sh
  suid-limited:
    - code: |
        ./ed
        !/bin/sh
---
