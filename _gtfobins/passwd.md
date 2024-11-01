---
functions:
  sudo:
    - code: |
        PASS=new_password_here
        echo -e "$PASS\n$PASS" | sudo passwd root
        su root
---
