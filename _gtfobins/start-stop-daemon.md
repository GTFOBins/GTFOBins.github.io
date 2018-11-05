---
functions:
  shell:
    - code: start-stop-daemon --start -x '/bin/sh'
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
