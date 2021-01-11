---
functions:
  file-read:
    - description: Outputs the first line of the file, until the first whitespace, to stderr.
      code: |
        LFILE=file_to_read
        bridge -b "${LFILE}"
---
