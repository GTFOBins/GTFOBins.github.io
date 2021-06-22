---
functions:
  shell:
    - code: yarn exec /bin/sh
    - code: |
         TF=$(mktemp -d)
         echo '{"scripts": {"shell": "/bin/sh"}}' > $TF/package.json
         yarn --cwd $TF run shell
  sudo:
    - code: sudo yarn exec /bin/sh
---
