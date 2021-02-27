---
description: This invokes the default pager, which is likely to be  [`less`](/gtfobins/less/), other functions may apply.
functions:
  shell:
    - code: |
        man man
        !/bin/sh
    - description: This only works for GNU `man` and requires GNU `troff` (`groff` to be installed).
      code: |
        man '-H/bin/sh #' man
  file-read:
    - code: man file_to_read
  sudo:
    - code: |
        sudo man man
        !/bin/sh
---
