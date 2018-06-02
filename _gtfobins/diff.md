---
functions:
  sudo-enabled:
    - code: |
        LFILE=file_to_read
        sudo diff --line-format=%L /dev/null $LFILE
  suid-enabled:
    - code: |
        LFILE=file_to_read
        ./diff --line-format=%L /dev/null $LFILE
  file-read:
    - code: |
        LFILE=file_to_read
        diff --line-format=%L /dev/null $LFILE
---
