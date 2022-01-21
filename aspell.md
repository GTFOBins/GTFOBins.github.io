---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        aspell -c "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./aspell -c "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo aspell -c "$LFILE"
---
