---
functions:
  file-read:
    - description: The file is read and parsed as an `expect` command file, the content of the first invalid line is returned in an error message. Thus, this might not be suitable to read arbitrary binary files.
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
