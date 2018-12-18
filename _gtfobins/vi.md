---
description: Modern Unix systems run [`vim`](/gtfobins/vim/) binary when `vi` is called.
functions:
  shell:
    - code: vi -c ':!/bin/sh' /dev/null
    - code: |
        vi
        :set shell=/bin/sh
        :shell
  file-write:
    - code: |
        vi file_to_write
        iDATA
        ^[
        w
  file-read:
    - code: vi file_to_read
  sudo:
    - code: sudo vi -c ':!/bin/sh' /dev/null
---
