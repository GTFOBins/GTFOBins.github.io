---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        diff --line-format=%L /dev/null $LFILE
  suid:
    - code: |
        LFILE=file_to_read
        ./diff --line-format=%L /dev/null $LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        sudo diff --line-format=%L /dev/null $LFILE
  directory-listing:
    - code: |
        LFOLDER=folder_to_list
        diff --recursive /any/folder $LFOLDER | grep $LFOLDER
---
