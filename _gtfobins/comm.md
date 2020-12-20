---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        comm $LFILE /dev/null 2>/dev/null
  suid:
    - code: |
        LFILE=file_to_read
        comm $LFILE /dev/null 2>/dev/null
  sudo:
    - code: |
        LFILE=file_to_read
        sudo comm $LFILE /dev/null 2>/dev/null
---
