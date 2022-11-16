---
functions:
  shell:
    - code: cabal exec -- /bin/sh
  limited-suid:
    - code: ./cabal exec -- /bin/sh -p
  sudo:
    - code: sudo cabal exec -- /bin/sh
---
