---
description: |
  This is the `check_by_ssh` Nagios plugin, available e.g. in `/usr/lib/nagios/plugins/`.
functions:
  command:
    - description: The host example.net must return a certificate via TLS
      code: |
        COMMAND=id
        OUTPUT=output_file
        TF=$(mktemp)
        echo "$COMMAND | tee $OUTPUT" > $TF
        chmod +x $TF
        check_ssl_cert --curl-bin $TF -H example.net
        cat $OUTPUT
  sudo:
    - description: The host example.net must return a certificate via TLS
      code: |
        COMMAND=id
        OUTPUT=output_file
        TF=$(mktemp)
        echo "$COMMAND | tee $OUTPUT" > $TF
        chmod +x $TF
        umask 022
        check_ssl_cert --curl-bin $TF -H example.net
        cat $OUTPUT
---
