---
description: This can be run with elevated privileges to change ownership and then read, write, or execute a file.
functions:
  suid:
    - code: |
        LFILE=file_to_change
        ./chown $(id -un):$(id -gn) $LFILE
  sudo:
    - code: |
        LFILE=file_to_change
        sudo chown $(id -un):$(id -gn) $LFILE
---
