---
description: The textual file is dumped on the current TTY (neither to `stdout` nor to `stderr`).
functions:
  sudo:
    - code: |
        LFILE=file_to_read
        sudo wall --nobanner "$LFILE"
---
