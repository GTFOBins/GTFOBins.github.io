---
description: |
  This is the `check_by_ssh` Nagios plugin, available e.g. in `/usr/lib/nagios/plugins/`.
functions:
  command:
    - code: |
        COMMAND=id
        OUTPUT=output_file
        TF=$(mktemp)
        echo "ProxyCommand $COMMAND | tee $OUTPUT" > $TF
        check_by_ssh -F $TF -H localhost -C something
        cat $OUTPUT
  sudo:
    - code: |
        COMMAND=id
        OUTPUT=output_file
        TF=$(mktemp)
        echo "ProxyCommand $COMMAND | tee $OUTPUT" > $TF
        sudo check_by_ssh -F $TF -H localhost -C something
        cat $OUTPUT
---
