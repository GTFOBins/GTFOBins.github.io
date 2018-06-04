---
description: |
  Three spaces are added before each character in the read file, and
  non-printable chars are printed as backslash escape sequences.
functions:
  sudo-enabled:
    - code: |
        LFILE=file_to_read
        sudo od -An -c -w9999 "$LFILE"
  suid-enabled:
    - code: |
        LFILE=file_to_read
        ./od -An -c -w9999 "$LFILE"
  file-read:
    - code: |
        LFILE=file_to_read
        od -An -c -w9999 "$LFILE"
---
