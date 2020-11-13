---
description: |
  This is the `check_raid` Nagios plugin, available e.g. in `/usr/lib/nagios/plugins/`. The read file content is limited to the first line.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        check_raid --extra-opts=@$LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        sudo check_raid --extra-opts=@$LFILE
---
