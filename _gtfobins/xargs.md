---
functions:
  execute-non-interactive:
    - code: xargs -a /dev/null /usr/bin/id
  sudo-enabled:
    - code: sudo xargs -a /dev/null /usr/bin/id
  suid-enabled:
    - code: ./xargs -a /dev/null /usr/bin/id
  file-read:
    - description: This relies on the fact the the file doesn't contain a null char (ASCII 0).
      code: xargs --arg-file=file_to_read -0 echo
---
