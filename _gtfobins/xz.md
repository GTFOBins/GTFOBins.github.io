---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        xz -c "$LFILE" | xz -d
  suid:
    - code: |
        LFILE=file_to_read
        ./xz -c "$LFILE" | xz -d
  sudo:
    - code: |
        LFILE=file_to_read
        sudo xz -c "$LFILE" | xz -d
---
