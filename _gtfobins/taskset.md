---
functions:
  shell:
    - code: taskset 1 /bin/sh
  suid:
    - code: ./taskset 1 /bin/sh -p
  sudo:
    - code: sudo taskset 1 /bin/sh
---
