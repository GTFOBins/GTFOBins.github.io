---
description: |
  This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.

  This might not work if run by unprivileged users depending on the system configuration.
functions:
  shell:
    - code: |
        loginctl user-status
        !/bin/sh
  sudo:
    - code: |
        sudo loginctl user-status
        !/bin/sh
---
