---
functions:
  shell:
    - code: tmate -c /bin/sh
  sudo:
    - code: sudo tmate -c /bin/sh
  suid-limited:
    - code: ./tmate -c /bin/sh
---
