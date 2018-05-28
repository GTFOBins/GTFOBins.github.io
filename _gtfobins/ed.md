---
functions:
  execute-interactive:
    - code: |
        ed
        !/bin/sh
  sudo-enabled:
    - code: |
        sudo ed
        !/bin/sh
  suid-limited:
    - code: |-
        ./ed
        !/bin/sh
  file-read:
    - code: |
        ed file_to_read
  file-write:
    - code: |
        ed file_to_write
        w
---
