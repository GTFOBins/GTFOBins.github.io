---
functions:
  shell:
    - code: yarn exec /bin/sh
    - description: Additionally, arbitrary script names can be used in place of `preinstall` and triggered by name with, e.g., `yarn --cwd $TF run preinstall`.
      code: |
        TF=$(mktemp -d)
        echo '{"scripts": {"preinstall": "/bin/sh"}}' > $TF/package.json
        yarn --cwd $TF install
  sudo:
    - code: sudo yarn exec /bin/sh
---
