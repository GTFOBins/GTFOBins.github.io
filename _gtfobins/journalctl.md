---
description: This might not work if run by unprivileged users depending on the system configuration.
functions:
  execute-interactive:
    - code: |
        journalctl
        !/bin/sh
  sudo-enabled:
    - code: |
        sudo journalctl
        !/bin/sh
---
