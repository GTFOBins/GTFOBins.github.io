---
description: A valid SMB/CIFS server must be available.
functions:
  execute-interactive:
    - code: |
        smbclient \\ip\share
        !/bin/sh
  sudo-enabled:
    - code: |
        sudo smbclient \\ip\share
        !/bin/sh
---
