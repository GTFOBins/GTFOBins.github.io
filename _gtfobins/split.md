---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        TF=$(mktemp)
        split $LFILE $TF
        cat $TF*
  command:
    - description: Command execution using an existing or newly created file.
      code: |
        COMMAND=id
        TF=$(mktemp)
        split --filter=$COMMAND $TF
    - description: Command execution using stdin (and close it directly).
      code: |
        COMMAND=id
        echo | split --filter=$COMMAND /dev/stdin
  shell:
    - description: The shell prompt is not printed.
      code: |
        split --filter=/bin/sh /dev/stdin
  sudo:
    - description: The shell prompt is not printed.
      code: |
        split --filter=/bin/sh /dev/stdin
---
