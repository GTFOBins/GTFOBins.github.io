---
functions:
  shell:
    - code: csh
  file-write:
    - code: |
        export LFILE=file_to_write
        ash -c 'echo DATA > $LFILE'
  suid:
    - code: "./csh -b"
  sudo:
    - code: sudo csh
---
