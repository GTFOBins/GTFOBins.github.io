---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        csplit $LFILE 1
        cat xx01
  file-write:
    - description: Writes the data to `xx0file_to_write`. If needed, a different prefix can be specified with `-f` (instead of `xx`).
      code: |
        TF=$(mktemp)
        echo "DATA" > $TF
        LFILE=file_to_write
        csplit -z -b "%d$LFILE" $TF 1
  suid:
    - code: |
        LFILE=file_to_read
        csplit $LFILE 1
        cat xx01
  sudo:
    - code: |
        LFILE=file_to_read
        csplit $LFILE 1
        cat xx01
---
