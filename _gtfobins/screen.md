---
functions:
  shell:
    - code: screen
  file-write:
    - description: This works on screen version 4.06.02. Data is appended to the file and `\n` is converted to `\r\n`.
      code: |
        LFILE=file_to_write
        screen -L -Logfile $LFILE echo DATA
    - description: This works on screen version 4.05.00. Data is appended to the file and `\n` is converted to `\r\n`.
      code: |
        LFILE=file_to_write
        screen -L $LFILE echo DATA
  sudo:
    - code: sudo screen
---
