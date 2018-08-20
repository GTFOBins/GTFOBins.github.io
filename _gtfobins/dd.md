---
functions:
  file-write:
    - code: |
        LFILE=file_to_write
        echo "DATA" | dd of=$LFILE
  file-read:
    - code: |
        LFILE=file_to_read
        dd if=LFILE
  suid-enabled:
    - code: |
        LFILE=file_to_write
        echo "data" | ./dd of=$LFILE
  sudo-enabled:
    - code: |
        LFILE=file_to_write
        echo "data" | sudo -E dd of=$LFILE
---
