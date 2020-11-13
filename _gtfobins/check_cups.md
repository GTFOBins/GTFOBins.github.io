---
description: |
  This is the `check_cups` Nagios plugin, available e.g. in `/usr/lib/nagios/plugins/`. The read file content is limited to the first line.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        check_cups --extra-opts=@$LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        sudo check_cups --extra-opts=@$LFILE
---
