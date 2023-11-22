---
functions:
  file-read:
    - description: The file is read and parsed as a `tmux` configuration file, part of the first invalid line is returned in an error message.
      code: |
        LFILE=file_to_read
        tmux -f $LFILE
  shell:
    - code: tmux
    - description: Provided to have enough permissions to access the socket.
      code: |
        tmux -S /path/to/socket_name
  sudo:
    - code: sudo tmux
---
