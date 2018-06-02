---
functions:
  execute-non-interactive:
    - description: The executed command output is not shown and can be redirected to a file.
      code: |
        export CMD="/usr/bin/id"
        puppet apply -e "exec { '${CMD}': }"
  sudo-enabled:
    - description: The executed command output is not shown and can be redirected to a file.
      code: |
        export CMD="/usr/bin/id"
        sudo puppet apply -e "exec { '${CMD}': }"
  file-read:
    - description: The read file content is corrupted by the `diff` output format.
      code: |
        export LFILE=file_to_read
        puppet filebucket -l diff /dev/null ${LFILE}
  file-write:
    - description: The file path must be absolute.
      code: |
        export LFILE="/tmp/file_to_write"
        puppet apply -e "file { '${LFILE}': content => 'data' }"
---
