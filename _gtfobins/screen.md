---
functions:
  shell:
    - code: screen
  file-write:
    - description: This has been found working on screen version 4.06.02. The file has a trailing `^C` character.
      code: |
        LFILE=file_to_write
        screen -L -Logfile $LFILE tail -f /dev/null
        DATA
        ^C
    - description: This has been found working on screen version 4.05.00. The file has a trailing `^C` character.
      code: |
        LFILE=file_to_write
        screen -L $LFILE tail -f /dev/null
        DATA
        ^C
  sudo:
    - code: sudo screen
---
