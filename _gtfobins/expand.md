---
description: 'The read file content is corrupted by replacing tabs with spaces.

'
functions:
  file-read:
  - code: |
      LFILE=file_to_read
      expand "$LFILE"
  suid-enabled:
  - code: |
      LFILE=file_to_read
      ./expand "$LFILE"
  sudo-enabled:
  - code: |
      LFILE=file_to_read
      sudo expand "$LFILE"
---
