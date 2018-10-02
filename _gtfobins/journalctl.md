---
functions:
  execute-interactive:
    - code: |
        journalctl --system
        !/bin/sh
  sudo-enabled:
    - code: |
        sudo journalctl
        !/bin/sh
---
