---
functions:
  file-write:
    - description: |
        Resulting file will contain additional timestamp lines in the format of `#1535795174` for each data line.
    - code: |
        LFILE=file_to_write
        HISTIGNORE='history *'
        history -c
        DATA
        history -w $LFILE
  file-read:
    - description: The file content will be surrounded by your current bash history session content.
    - code: |
        LFILE=file_to_read
        HISTTIMEFORMAT=$'\r\e[K'
        history -r $LFILE
        history
  sudo-enabled:
    - code: |
        LFILE=file_to_read
        sudo bash -c "HISTTIMEFORMAT=$'\r\e[K' && history -r $LFILE && history"
---
