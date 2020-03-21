---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        cp "$LFILE" /dev/stdout
  suid:
    - description: This can be used to copy and then read or write files from a restricted file systems or with elevated privileges.
      code: |
        LFILE=file_to_write
        TF=$(mktemp)
        echo "DATA" > $TF
        ./cp $TF $LFILE
  sudo:
    - description: This can be used to copy and then read or write files from a restricted file systems or with elevated privileges.
      code: |
        LFILE=file_to_write
        TF=$(mktemp)
        echo "DATA" > $TF
        sudo cp $TF $LFILE
---
