---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        wall --nobanner "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo wall --nobanner "$LFILE"
---
