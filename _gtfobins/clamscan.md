---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        TF=$(mktemp -d)
        touch $TF/empty.yara
        clamscan --no-summary -d $TF -f $LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        TF=$(mktemp -d)
        touch $TF/empty.yara
        sudo clamscan --no-summary -d $TF -f $LFILE
---
