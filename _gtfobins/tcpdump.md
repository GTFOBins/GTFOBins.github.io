---
description: These require some traffic to be actually captured. Also note that the subprocess is immediately sent to the background.
functions:
  execute-non-interactive:
    - code: |
        COMMAND='id'
        TF=$(mktemp)
        echo "$COMMAND" > $TF
        chmod +x $TF
        tcpdump -ln -i lo -w /dev/null -W 1 -G 1 -z $TF
  sudo-enabled:
    - code: |
        COMMAND='id'
        TF=$(mktemp)
        echo "$COMMAND" > $TF
        chmod +x $TF
        sudo tcpdump -ln -i lo -w /dev/null -W 1 -G 1 -z $TF
---
