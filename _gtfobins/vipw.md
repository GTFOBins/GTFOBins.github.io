---
functions:

  file-write:
    - code: |
        vipw --passwd
        vipw --shadow
  suid:
    - code: |
        ./vipw --passwd
  sudo:
    - code: sudo vipw --shadow
---
