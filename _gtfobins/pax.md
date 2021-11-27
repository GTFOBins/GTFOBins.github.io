---
functions:
  file-read:
    - description: The output is a `tar` archive containing the read file as it is, hence this may not be suitable to read arbitrary binary files.
      code: |
        LFILE=file_to_read
        pax -w "$LFILE"
---
