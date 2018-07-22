---
functions:
  execute-non-interactive:
    - code: |
        export PAGER=/usr/bin/id
        git -p help
  suid-limited:
    - code: |
        export PAGER=/usr/bin/id
        ./git -p help
  sudo-enabled:
    - code: |
        export PAGER=/usr/bin/id
        sudo -E git -p help
---
