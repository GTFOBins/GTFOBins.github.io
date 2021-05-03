---
functions:
  file-write:
    - description: The data to be written appears amid the syscall log, quoted and with special characters escaped in octal notation. The string representation will be truncated, pick a value big enough. More generally, any binary that executes whatever syscall passing arbitrary data can be used in place of `strace - DATA`.
      code: |
        LFILE=file_to_write
        strace -s 999 -o $LFILE strace - DATA
  shell:
    - code: strace -o /dev/null /bin/sh
  suid:
    - code: ./strace -o /dev/null /bin/sh -p
  sudo:
    - code: sudo strace -o /dev/null /bin/sh
---
