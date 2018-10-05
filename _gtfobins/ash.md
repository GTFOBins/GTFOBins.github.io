---
functions:
  shell:
    - code: ash
  file-write:
    - code: |
        export LFILE=file_to_write
        ash -c 'echo DATA > $LFILE'
  suid:
    - code: "./ash"
  sudo:
    - code: sudo ash
---
