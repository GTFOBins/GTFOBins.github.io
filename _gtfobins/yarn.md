---
functions:
  shell:
    - code: yarn exec /bin/sh
    - code: |
        TF=$(mktemp -d)
        echo '{"scripts": {"preinstall": "/bin/sh"}}' > $TF/package.json
        yarn --cwd $TF install
  sudo:
    - code: sudo yarn exec /bin/sh
---
