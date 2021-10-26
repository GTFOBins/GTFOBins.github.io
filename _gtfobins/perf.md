---
functions:
  shell:
    - code: |
        perf stat /bin/sh
  suid:
    - code: |
        ./perf stat /bin/sh -p
  sudo:
    - code: |
        sudo perf stat /bin/sh
---
