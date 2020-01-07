---
functions:
  shell:
    - code: dash
  file-write:
    - code: |
        export LFILE=file_to_write
        dash -c 'echo DATA > $LFILE'
  suid:
    - code: ./dash -p
  sudo:
    - code: sudo dash
---
