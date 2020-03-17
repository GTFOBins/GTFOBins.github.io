---
functions:
  file-read:
    - description: The read file content is corrupted by randomizing the order of NUL terminated strings.
      code: |
        LFILE=file_to_read
        shuf -z "$LFILE"
  file-write:
    - description: The written file content is corrupted by adding a newline.
      code: |
        LFILE=file_to_write
        shuf -e DATA -o "$LFILE"
  suid:
    - description: The written file content is corrupted by adding a newline.
      code: |
        LFILE=file_to_write
        ./shuf -e DATA -o "$LFILE"
  sudo:
    - description: The written file content is corrupted by adding a newline.
      code: |
        LFILE=file_to_write
        sudo shuf -e DATA -o "$LFILE"
---
