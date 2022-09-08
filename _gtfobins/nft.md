---
description: The content is actually parsed and corrupted by the command, thus it may not be suitable for arbitrary files. This requires version `nftables` v0.9.0.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        nft -f "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./nft -f "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo nft -f "$LFILE"
---
