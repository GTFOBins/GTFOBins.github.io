---
functions:
  shell:
    - code: yash -c /bin/sh
  suid:
    - code: ./yash -c '/bin/sh -p'
  sudo:
    - code: sudo yash -c /bin/sh
---
