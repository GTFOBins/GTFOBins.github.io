---
functions:
  sudo-enabled:
    - code: |
        LFILE=file_to_read
        sudo sed -e '' "$LFILE"
  suid-enabled:
    - code: |
        LFILE=file_to_read
        ./sed -e '' "$LFILE"
  file-read:
    - code: |
        LFILE=file_to_read
        sed -e '' "$LFILE"
---
