---
functions:
  file-read:
    - description: Each line is corrupted by a prefix string and wrapped inside quotes, so this may not be suitable for binary files. If a line in the target file begins with a `#`, it will not be printed as these lines are parsed as comments. Furthermore, if a line in the target file begins with a number or `>`, these characters are not printed. It can also be provided with a directory and will read each file in the directory.
      code: |
        LFILE=file_to_read
        file -m $LFILE
    - description: The specified file is used as a list of filenames for the `file` command. For each line (filename) in the specified file, the according filetype is determined. The line is printed independent if the file exists or not. Lines starting with `#`, numbers or `>` are also shown. For binary files, it's still not suitable.
      code: |
        LFILE=file_to_read
        file -f $LFILE
  suid:
    - description: Each line is corrupted by a prefix string and wrapped inside quotes, so this may not be suitable for binary files. If a line in the target file begins with a `#`, it will not be printed as these lines are parsed as comments. Furthermore, if a line in the target file begins with a number or `>`, these characters are not printed. It can also be provided with a directory and will read each file in the directory.
      code: |
        LFILE=file_to_read
        ./file -m $LFILE
    - description: The specified file is used as a list of filenames for the `file` command. For each line (filename) in the specified file, the according filetype is determined. The line is printed independent if the file exists or not. Lines starting with `#`, numbers or `>` are also shown. For binary files, it's still not suitable.
      code: |
        LFILE=file_to_read
        file -f $LFILE
  sudo:
    - description: Each line is corrupted by a prefix string and wrapped inside quotes, so this may not be suitable for binary files. If a line in the target file begins with a `#`, it will not be printed as these lines are parsed as comments. Furthermore, if a line in the target file begins with a number or `>`, these characters are not printed. It can also be provided with a directory and will read each file in the directory.
      code: |
        LFILE=file_to_read
        sudo file -m $LFILE
    - description: The specified file is used as a list of filenames for the `file` command. For each line (filename) in the specified file, the according filetype is determined. The line is printed independent if the file exists or not. Lines starting with `#`, numbers or `>` are also shown. For binary files, it's still not suitable.
      code: |
        LFILE=file_to_read
        file -f $LFILE
---
