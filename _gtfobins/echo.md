---
functions:
  file-read:
    - description: Read a file with only bash primitives and echo.
      code: |
        LFILE=file_to_read
        echo "$(<$LFILE)"
---
