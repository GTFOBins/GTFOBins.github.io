---
functions:
  file-read:
  - code: |-
      expect /path/to/input-file
    comment: |-
      The file is read and parsed as an `expect` command file, the content of the first invalid line is returned in an error message.
    contexts:
      sudo:
      suid:
      unprivileged:
  shell:
  - code: |-
      expect -c 'spawn /bin/sh;interact'
    contexts:
      sudo:
      suid:
        code: |-
          expect -c 'spawn /bin/sh -p;interact'
        shell: false
      unprivileged:
...
