---
functions:
  shell:
      code: |
        perf stat bash -p
  suid:
      code: |
        perf stat bash -p
  sudo:
      code: |
        sudo perf stat bash -p
---
