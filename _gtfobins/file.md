---
functions:
  file-read:
    - description: Each input line is treated as a filename for the `file` command and the output is corrupted by a suffix `:` followed by the result or the error of the operation, so this may not be suitable for binary files.
      code: |
        LFILE=file_to_read
        file -f $LFILE
    - description: |
        Each line is corrupted by a prefix string and wrapped inside quotes, so this may not be suitable for binary files.

        If a line in the target file begins with a `#`, it will not be printed as these lines are parsed as comments.

        It can also be provided with a directory and will read each file in the directory.
      code: |
        LFILE=file_to_read
        file -m $LFILE
  suid:
    - description: Each input line is treated as a filename for the `file` command and the output is corrupted by a suffix `:` followed by the result or the error of the operation, so this may not be suitable for binary files.
      code: |
        LFILE=file_to_read
        ./file -f $LFILE
  sudo:
    - description: Each input line is treated as a filename for the `file` command and the output is corrupted by a suffix `:` followed by the result or the error of the operation, so this may not be suitable for binary files.
      code: |
        LFILE=file_to_read
        sudo file -f $LFILE
---
