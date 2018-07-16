---
functions:
  execute-interactive:
    - code: |
        ed
        !/bin/sh
  file-write:
    - code: |
        ed file_to_write
        w
  file-read:
    - code: ed file_to_read
  sudo-enabled:
    - code: |
        sudo ed
        !/bin/sh
  suid-limited:
    - code: |
        ./ed
        !/bin/sh
---
