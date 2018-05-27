---
functions:
  execute-non-interactive:
    - code: watch /usr/bin/id
  sudo-enabled:
    - code: watch /usr/bin/id
  suid-enabled:
    - description: |-
        If present, maintain the SUID privileges with the `-x` option that uses `exec` instead of `sh -c`.
      code: watch -x /usr/bin/id
  suid-limited:
    - code: watch /usr/bin/id
---
