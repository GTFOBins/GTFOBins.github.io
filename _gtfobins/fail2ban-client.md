---
description: |
  The subprocess is immediately sent to the background, but `fail2ban-client` waits on a return code from the subprocess. The `banip` command will hang until the subprocess returns.
functions:
  sudo:
    - code: |
        COMMAND="id"
        sudo fail2ban-client add woot
        sudo fail2ban-client set woot addaction wootaction
        sudo fail2ban-client set woot action wootaction actionban "$COMMAND"
        sudo fail2ban-client start woot
        sudo fail2ban-client set woot banip 999.999.999.999
        sudo fail2ban-client set woot unbanip 999.999.999.999
        sudo fail2ban-client stop woot
---
