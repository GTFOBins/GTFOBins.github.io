---
functions:
  file-write:
    - description: write to a file.
      code: |
        LFILE=file_to_write
        TF=$(mktemp)
        echo ":DATA">$TF
        ltrace -s 999 -e fgets --output=$LFILE ltrace --config=$TF $(mktemp)
  shell:
    - code: ltrace -b -L /bin/sh
  sudo:
    - code: sudo ltrace -b -L /bin/sh
---
