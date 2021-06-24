---
functions:
  file-read:
    - description: The file is read and parsed as a `tmux` configuration file, part of the first invalid line is returned in an error message.
      code: |
        LFILE=file_to_read
        tmux -f $LFILE
  shell:
    - code: tmux
  sudo:
    - code: sudo tmux
---
