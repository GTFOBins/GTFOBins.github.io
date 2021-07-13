---
description: Dump the bytes of the input file that are different from the NUL byte in a tabular format, hence this may not be suitable to read arbitrary binary files.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        cmp $LFILE /dev/zero -b -l
  suid:
    - code: |
        LFILE=file_to_read
        ./cmp $LFILE /dev/zero -b -l
  sudo:
    - code: |
        LFILE=file_to_read
        sudo cmp $LFILE /dev/zero -b -l
---
