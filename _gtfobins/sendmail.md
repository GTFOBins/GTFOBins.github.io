---
functions:
  sudo:
    - code: |
        LFILE=file_to_read
        sudo /usr/bin/sendmail -tf aaa -C$LFILE
---
