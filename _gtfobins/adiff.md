---
functions:
  file-read:
    - description: Read files from archives when utils like "tar" are missing.
      code: |
        OUTFILE=$(mktemp -u)
        LFILE=file_to_read
        ar r "${OUTFILE}" "${LFILE}"
        adiff "${OUTFILE}" /dev/null
        ls -la Unpack*
---
