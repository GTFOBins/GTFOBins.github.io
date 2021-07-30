---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        csplit $LFILE 1
        cat xx01
  file-write:
    - description: -f flag use PREFIX instead of 'xx', using path like "/tmp/data.txt" as a PREFIX will output the file in /tmp/ with names data.txt00,data.txt01
      code: |
        TEMP=$(mktemp)
        echo "DATA" > $TEMP
        LFILE=file-to-write
        csplit $TEMP 1 -f $LFILE
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
