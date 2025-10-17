---
functions:
  file-read:
    - description: It reads data from files, it may be used to do privileged reads or disclose files outside a restricted file system. The output might be corrupted or incomplete if the file does not follow the expected database format. Available in util-linux on CentOS, RHEL, Fedora. 
      code: |
        LFILE=file_to_read
        last -f $LFILE -a
  sudo:
    - description: If the binary is allowed to run as superuser by sudo, it does not drop the elevated privileges and may be used to access the file system, escalate or maintain privileged access.
      code: |
        LFILE=file_to_read
        last -f $LFILE -a
---
