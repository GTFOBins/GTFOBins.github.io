---
functions:
  execute-interactive:
    - code: |
        man man
        !/bin/sh
  sudo-enabled:
    - code: |
        sudo man man
        !/bin/sh
  suid-limited:
    - code: |
        ./man man
        !/bin/sh
  file-read:
    - code: |
        man file_to_read
---
