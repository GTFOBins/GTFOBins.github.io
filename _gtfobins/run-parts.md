---
functions:
  shell:
    - code: run-parts --new-session --regex '^sh$' /bin
  sudo:
    - code: sudo run-parts --new-session --regex '^sh$' /bin
  suid:
    - code: ./run-parts --new-session --regex '^sh$' /bin --arg='-p'
---
