---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        TF=$(mktemp -d)
        touch $TF/empty.yara
        clamscan --no-summary -d $TF -f $LFILE 2>&1 | sed -nE 's/^(.*): No such file or directory$/\1/p'
  sudo:
    - code: |
        LFILE=file_to_read
        TF=$(mktemp -d)
        touch $TF/empty.yara
        sudo clamscan --no-summary -d $TF -f $LFILE 2>&1 | sed -nE 's/^(.*): No such file or directory$/\1/p'
---
