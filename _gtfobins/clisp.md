---
functions:
  shell:
    - code: clisp -x '(ext:run-shell-command "sh") (ext:exit)'
  sudo:
    - code: sudo clisp -x '(ext:run-shell-command "sh") (ext:exit)'
---
