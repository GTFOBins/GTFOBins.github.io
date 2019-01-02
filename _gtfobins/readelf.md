---
description: |
  Each line is corrupted by a prefix string and wrapped inside single quotes. Also consider that lines are actually parsed as `readelf` options thus some file contents may lead to unexpected results.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        readelf -a @$LFILE
  suid:
    - code: |
        LFILE=file_to_read
        ./readelf -a @$LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        sudo readelf -a @$LFILE
---
