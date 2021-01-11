---
functions:
  file-read:
      code: |
        OUTFILE=$(mktemp -u)
        LFILE=file_to_read
        ar r "${OUTFILE}" "${LFILE}"
        cat "${OUTFILE}"
---
