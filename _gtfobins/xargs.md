---
functions:
  execute-non-interactive:
    - code: echo yyy | xargs -Ixxx /usr/bin/id
  sudo-enabled:
    - code: echo yyy | sudo xargs -Ixxx /usr/bin/id
  suid-enabled:
    - code: echo yyy | xargs -Ixxx /usr/bin/id
---
