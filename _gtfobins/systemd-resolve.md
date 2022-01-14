---
functions:
  sudo:
    - description: This invokes the default pager, which is likely to be [`less`](../less/index.html), other functions may apply.
      code: |
        sudo systemd-resolve --status
        !sh
---
