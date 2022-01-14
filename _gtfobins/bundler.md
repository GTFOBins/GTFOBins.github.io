---
functions:
  shell:
    - description: This invokes the default pager, which is likely to be  [`less`](../less/index.html), other functions may apply.
      code: |
        bundler help
        !/bin/sh
    - code: |
        export BUNDLE_GEMFILE=x
        bundler exec /bin/sh
    - code: |
        TF=$(mktemp -d)
        touch $TF/Gemfile
        cd $TF
        bundler exec /bin/sh
    - description: This spawns an interactive shell via [`irb`](../irb/index.html).
      code: |
        TF=$(mktemp -d)
        touch $TF/Gemfile
        cd $TF
        bundler console
        system('/bin/sh -c /bin/sh')
    - code: |
        TF=$(mktemp -d)
        echo 'system("/bin/sh")' > $TF/Gemfile
        cd $TF
        bundler install
  sudo:
    - description: This invokes the default pager, which is likely to be  [`less`](../less/index.html), other functions may apply.
      code: |
        sudo bundler help
        !/bin/sh
---
