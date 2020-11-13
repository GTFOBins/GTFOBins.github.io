---
functions:
  shell:
    - code: |
        ex
        !sh
  file-write:
    - code: |
        ex file_to_write
        a
        DATA
        .
        w
        q
  file-read:
    - code: |
        ex file_to_read
        ,p
        q
  sudo:
    - code: |
        sudo ex
        !sh
  suid:
    - code: |
        ./ex
        !sh -p
---
