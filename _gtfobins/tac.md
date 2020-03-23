---
functions:
  file-read:
    - description: It reads data from files, it may be used to do privileged reads or disclose files outside a restricted file system.
      code: |
        LFILE=file_to_read
        tac "$LFILE"
---
