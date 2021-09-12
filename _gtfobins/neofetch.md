---
description: The file content is used as the logo while some other information is displayed on its right, thus it might not be suitable to read arbitray binary files.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        neofetch --ascii $LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        sudo neofetch --ascii $LFILE
---
