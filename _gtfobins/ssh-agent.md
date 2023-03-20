---
functions:
  command:
    - code: |
        COMMAND=id
        ssh-agent "$COMMAND"
  shell:
    - code: ssh-agent sh
  suid:
    - code: ssh-agent sh -p
  sudo:
    - code: sudo ssh-agent sh
---
