---
functions:
  execute-non-interactive:
    - code: |
        export CMD="/usr/bin/id"
        puppet apply -e "exec { '${CMD}': }"
  sudo-enabled:
    - code: |
        export CMD="/usr/bin/id"
        sudo puppet apply -e "exec { '${CMD}': }"
  file-read:
    - code: |
        export LFILE=file_to_read
        puppet filebucket -l diff /dev/null ${LFILE}
  file-write:
    - code: |
        export LFILE="/tmp/file_to_write"
        puppet apply -e "file { '${LFILE}': content => 'data' }"
---
