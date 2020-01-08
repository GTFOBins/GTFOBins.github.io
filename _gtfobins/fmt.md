---
description: The read file content is not binary-safe.
functions:
  file-read:
    - description: This only works for the GNU version of `fmt`.
      code: |
        LFILE=file_to_read
        fmt -pNON_EXISTING_PREFIX "$LFILE"
    - description: This corrupts the output by wrapping very long lines at the given width.
      code: |
        LFILE=file_to_read
        fmt -999 "$LFILE"
  suid:
    - description: This corrupts the output by wrapping very long lines at the given width.
      code: |
        LFILE=file_to_read
        ./fmt -999 "$LFILE"
  sudo:
    - description: This corrupts the output by wrapping very long lines at the given width.
      code: |
        LFILE=file_to_read
        sudo fmt -999 "$LFILE"
---
