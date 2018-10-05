---
functions:
  shell:
    - code: PAGER='sh -c "exec sh 0<&1"' git -p help
  sudo:
    - code: PAGER='sh -c "exec sh 0<&1"' sudo -E git -p help
  limited-suid:
    - code: PAGER='sh -c "exec sh 0<&1"' ./git -p help
---
