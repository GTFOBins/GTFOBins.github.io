---
functions:
  shell:
    - code: tcsh
  file-write:
    - code: |
        export LFILE=file_to_write
        tcsh -c 'echo DATA > $LFILE'
  suid:
    - code: "./tcsh -b"
  sudo:
    - code: sudo tcsh
---
