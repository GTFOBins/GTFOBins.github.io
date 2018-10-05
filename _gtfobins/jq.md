---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        jq -Rr . "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./jq -Rr . "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo jq -Rr . "$LFILE"
---
