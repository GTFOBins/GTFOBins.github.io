---
functions:
  shell:
    - description: GNU version only.
      code: xargs -a /dev/null sh
    - code: echo x | xargs -Iy sh -c 'exec sh 0<&1'
    - description: Read interactively from `stdin`.
      code: |
        xargs -Ix sh -c 'exec sh 0<&1'
        x^D^D
  file-read:
    - description: This works as long as the file does not contain the NUL character, also a trailing `$'\n'` is added. The actual `/bin/echo` command is executed. GNU version only.
      code: |
        LFILE=file_to_read
        xargs -a "$LFILE" -0
  suid:
    - description: GNU version only.
      code: ./xargs -a /dev/null sh -p
  sudo:
    - description: GNU version only.
      code: sudo xargs -a /dev/null sh
---
