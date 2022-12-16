---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        pandoc -t plain "$LFILE"
  file-write:
    - code: |
        LFILE=file_to_write
        echo DATA | pandoc -t plain -o "$LFILE"
  suid:
    - code: |
        LFILE=file_to_write
        echo DATA | ./pandoc -t plain -o "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_write
        echo DATA | sudo pandoc -t plain -o "$LFILE"
---
