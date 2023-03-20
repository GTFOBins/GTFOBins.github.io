---
functions:
  file-read:
    - code: |
        export LFILE=file_to_write
        elvish -c 'cat $E:LFILE'
  file-write:
    - code: |
        export LFILE=file_to_write
        elvish -c 'echo DATA > $E:LFILE'
  shell:
    - code: elvish
  sudo:
    - code: sudo elvish
---
