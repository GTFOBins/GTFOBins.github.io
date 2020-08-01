---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        history -r "$FILE"
        history
  file-write:
    - code: |
        WFILE=file_to_WRITE
        history -c #Clears current bash_history file
        #Write data in command line
        history -w #WFILE		
  suid:
    - code: |
        LFILE=file_to_LOAD
        WFILE=file_to_WRITE
        history -c #Clears current bash_history file
        history -r $LFILE; history -w #WFILE
    - code: |
        LFILE=file_to_read
        history -r "$FILE"
        history     
  sudo:
    - code: |
        LFILE=file_to_LOAD
        WFILE=file_to_WRITE
        history -c #Clears current bash_history file
        history -r $LFILE; history -w #WFILE
    - code: |
        LFILE=file_to_read
        history -r "$FILE"
        history      
---
