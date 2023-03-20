---
functions:
  file-read:
    - code: |
        export LFILE=file_to_read
        elvish -c 'echo (slurp <$E:LFILE)'
  file-write:
    - code: |
        export LFILE=file_to_write
        elvish -c 'echo DATA >$E:LFILE'
  shell:
    - code: elvish
  suid:
    - code: ./elvish
  sudo:
    - code: sudo elvish
---
