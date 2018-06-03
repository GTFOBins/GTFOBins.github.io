---
functions:
  execute-interactive:
    - code: rlwrap /bin/sh
  sudo-enabled:
    - code: sudo rlwrap /bin/sh
  suid-enabled:
    - code: ./rlwrap -H /tmp/y /bin/sh -p
  file-write:
    - description: This adds timestamps to the output file.
      code: |
        LFILE=file_to_write
        rlwrap -l "$LFILE" echo data
---
