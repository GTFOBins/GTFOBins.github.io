---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        TF=$(mktemp)
        split $LFILE $TF
        cat $TF*
  command:
    - description: Command execution using an existing or new created file.
      code: |
        COMMAND=id
        TF=$(mktemp)
        split --filter=$COMMAND $TF
    - description: Command execution using stdin (and close it directly).
      code: |
        COMMAND=id
        echo | split --filter=$COMMAND /dev/stdin
  shell:
    - code: |
        split --filter=bash /dev/stdin
  sudo:
    - code: |
        split --filter=bash /dev/stdin
---
