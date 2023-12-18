---
description: The read file content is binary-safe.
functions:
  file-read:
    - code: |
        export LFILE="file_to_read"
        (exec < "$LFILE"; tr -d "")
---
