---
functions:
  shell:
    - code: cabal exec -- /bin/sh
  suid:
    - code: ./cabal exec -- /bin/sh -p
  sudo:
    - code: sudo cabal exec -- /bin/sh
---
