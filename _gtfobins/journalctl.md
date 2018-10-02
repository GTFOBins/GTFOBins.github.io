---
functions:
  execute-interactive:
    - description: This might not work if run by unprivileged users depending on the system configuration.
      code: |
        journalctl --system
        !/bin/sh
  sudo-enabled:
    - code: |
        sudo journalctl
        !/bin/sh
---
