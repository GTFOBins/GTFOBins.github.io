---
description: ntpdate, a command-line utility for clock synchronization using NTP.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        ntpdate -a key -k $LFILE -d localhost
  sudo:
    - code: |
        LFILE=file_to_read
        sudo ntpdate -a key -k $LFILE -d localhost
---