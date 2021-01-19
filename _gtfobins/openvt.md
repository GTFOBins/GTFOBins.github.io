---
functions:
  sudo:
    - description: If the binary is allowed to run as superuser by sudo, it does not drop the elevated privileges and may be used to access the file system, escalate or maintain privileged access.
      code: |
        sudo openvt -vsu bash
---
