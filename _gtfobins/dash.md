---
functions:
  shell:
    - code: dash
  file-write:
    - code: |
        export LFILE=file_to_write
        ash -c 'echo DATA > $LFILE'
  suid:
    - code: ./dash -p
  sudo:
    - code: sudo dash
---
