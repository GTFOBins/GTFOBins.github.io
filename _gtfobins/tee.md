---
description: 'It can only append data if the destination exists.

'
functions:
  file-write:
  - code: |
      LFILE=file_to_write
      echo data | ./tee -a "$LFILE"
  suid-enabled:
  - code: |
      LFILE=file_to_write
      echo data | ./tee -a "$LFILE"
  sudo-enabled:
  - code: |
      LFILE=file_to_write
      echo data | sudo tee -a "$LFILE"
---
