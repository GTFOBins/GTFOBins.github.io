---
description: It can be used to generate core dumps of running processes. Such files often contains sensitive information such as open files content, cryptographic keys, passwords, etc. This command produces a binary file named `core.$PID`, that is then often filtered with `strings` to narrow down relevant information.
functions:
  file-read:
    - code: gcore $PID
  sudo:
    - code: sudo gcore $PID
  suid:
    - code: ./gcore $PID
---
