---
functions:
  description:
    A newline char is added to the data.  The data may contain several lines: `shuf -e $'line 1\nline 2\nline 3' -o file_to_write`
  sudo-enabled:
    - code: |
        LFILE=file_to_write
        sudo shuf -e data -o "$LFILE"
  suid-enabled:
    - code: |
        LFILE=file_to_write
        ./shuf -e data -o "$LFILE"
  file-write:
    - code: |
        LFILE=file_to_write
        shuf -e data -o "$LFILE"
---
