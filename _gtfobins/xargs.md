---
functions:
  execute-non-interactive:
    - code: xargs -a /dev/null /usr/bin/id
  sudo-enabled:
    - code: sudo xargs -a /dev/null /usr/bin/id
  suid-enabled:
    - code: ./xargs -a /dev/null /usr/bin/id
  file-read:
    - description: This works as long as the file does not contain the NUL character, also a trailing `$'\n'` is added. The actual `/bin/echo` command is executed. GNU version only.
      code: |
        LFILE=file_to_read
        xargs -a "$LFILE" -0
---
