---
functions:
  execute-non-interactive:
    - code: xargs -a /dev/null /usr/bin/id
  sudo-enabled:
    - code: sudo xargs -a /dev/null /usr/bin/id
  suid-enabled:
    - code: ./xargs -a /dev/null /usr/bin/id
---
