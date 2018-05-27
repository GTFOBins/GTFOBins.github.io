---
functions:
  execute-non-interactive:
    - code: watch /usr/bin/id
  sudo-enabled:
    - code: watch /usr/bin/id
  suid-enabled:
    - description: This keeps the SUID privileges only if the `-x` option is present.
      code: watch -x /usr/bin/id
  suid-limited:
    - code: watch /usr/bin/id
---
