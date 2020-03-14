---
functions:
  file-read:
    - description: This spawns a graphical window containing the file content somehow corrupted by word wrapping, it might not be suitable to read arbitrary files. The path must be absolute.
      code: |
        LFILE=file_to_read
        yelp "man:$LFILE"
---
