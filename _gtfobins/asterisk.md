---
functions:
  shell:
    - description: Connect to the Asterisk console and drop into a shell
      code: |
        asterisk -r
      code: |
        !sh
  sudo:
    - description: Start Asterisk as root in the foreground to create its CLI socket
      code: |
        sudo asterisk -F
    - description: Connect to the Asterisk console as root and drop into a shell
      code: |
        sudo asterisk -r
      code: |
        !sh
---
