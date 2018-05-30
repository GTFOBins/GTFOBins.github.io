---
functions:
  execute-interactive:
    - code: unshare /bin/sh
  sudo-enabled:
    - code: sudo unshare /bin/sh
  suid-enabled:
    - description: This keeps the SUID privileges only if the `-r` option is present.
      code: ./unshare -r /bin/sh
  suid-limited:
    - code: ./unshare /bin/sh
---
