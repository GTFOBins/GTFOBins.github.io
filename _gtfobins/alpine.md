---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        alpine -F "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./alpine -F "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo alpine -F "$LFILE"
---
