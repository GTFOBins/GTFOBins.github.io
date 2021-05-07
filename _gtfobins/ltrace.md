---
functions:
  file-write:
    code: |
        LFILE=file_to_write
        WFILE=$(mktemp)
        echo ":DATA">$WFILE
        ltrace -s 999 -e fgets --output=$LFILE ltrace --config=$WFILE $(mktemp)
  file-read:
    code: |
        LFILE=file_to_read
        ltrace --config=$LFILE $(mktemp)
  shell:
    - code: ltrace -b -L /bin/sh
  sudo:
    - code: sudo ltrace -b -L /bin/sh
---
