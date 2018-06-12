---
functions:
  sudo-enabled:
    - code: |
        LFILE=file_to_read
        sudo jq -Rr . "$LFILE"
  suid-enabled:
    - code: |
        LFILE=file_to_read
        ./jq -Rr . "$LFILE"
  file-read:
    - code: |
        LFILE=file_to_read
        jq -Rr . "$LFILE"
---
