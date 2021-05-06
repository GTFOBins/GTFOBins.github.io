---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        lwp-request "file://$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo lwp-request "file://$LFILE"
---
