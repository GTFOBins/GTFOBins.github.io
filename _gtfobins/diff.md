---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        diff --line-format=%L /dev/null $LFILE
    - description: This lists the content of a directory. `$TF` can be any directory, but for convenience it is better to use an empty directory to avoid noise output.
      code: |
        LFOLDER=folder_to_list
        TF=$(mktemp -d)
        diff --recursive $TF $LFOLDER
  suid:
    - code: |
        LFILE=file_to_read
        ./diff --line-format=%L /dev/null $LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        sudo diff --line-format=%L /dev/null $LFILE
---
