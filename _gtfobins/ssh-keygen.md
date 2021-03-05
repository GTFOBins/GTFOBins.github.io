---
functions:
  library-load:
    - description: |
      code: ssh-keygen -D ./lib.so
  sudo:
    - description: |
      code: sudo ssh-keygen -D ./lib.so
  suid:
    - description: |
      code: ./ssh-keygen -D ./lib.so
---
