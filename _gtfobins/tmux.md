---
functions:
  file-read:
    - description: The file is read and parsed as an `tmux` command file, the content of the first invalid line is returned in an error message.
      code: |
        LFILE=file_to_read
        tmux -f $LFILE
  shell:
    - code: tmux
  sudo:
    - code: sudo tmux
---
