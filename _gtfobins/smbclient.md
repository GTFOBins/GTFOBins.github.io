---
description: A valid SMB/CIFS server must be available.
functions:
  shell:
    - code: |
        smbclient \\ip\share
        !/bin/sh
  sudo:
    - code: |
        sudo smbclient \\ip\share
        !/bin/sh
---
