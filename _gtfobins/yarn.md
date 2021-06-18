---
description: Yarn is a tool which similar to npm. It is used for installing npm packages.
functions:
  shell:
    - description: If the binary is running without `sudo`, it can be used to break out from restricted environments by spawning an interactive system shell.
      code: yarn exec /bin/bash/
    - ....
  sudo:
    - description: If the binary is allowed to run as superuser by `sudo`, it can be use to spawn `root` shell.
      code: sudo yarn exec /bin/bash/
    - ...
  ...
---
