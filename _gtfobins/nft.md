---
description: It is possible to read files with nft
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        sudo nft -f "$LFILE"
---
