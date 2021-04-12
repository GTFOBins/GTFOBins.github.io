---
functions:
  shell:
    - code: ash
  file-write:
    - code: |
        export LFILE=file_to_write
        ash -c 'echo DATA > $LFILE'
  file-read:
    - code: |
        ash -c "echo $(</file/to/read.txt)"
  suid:
    - code: "./ash"
  sudo:
    - code: sudo ash
---
