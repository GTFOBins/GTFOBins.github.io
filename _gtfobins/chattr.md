---
description: |
  chattr is a Linux utility to change file attributes on ext2/3/4 filesystems.
  It can be abused in privilege escalation scenarios when misconfigured
  (e.g., via sudo or SUID), allowing attackers to set immutable attributes
  on sensitive files.

functions:
  privesc:
    - description: |
        If chattr is allowed via sudo, it can be used to set the immutable
        attribute on files like /etc/sudoers or /etc/passwd, preventing
        administrators from modifying them and enabling persistence or
        privilege escalation.
      code: |
        sudo chattr +i /etc/sudoers
    - description: |
        If chattr is misconfigured with SUID, a user can lock critical files
        to block root changes or enforce malicious configurations.
      code: |
        ./chattr +i /etc/shadow

contexts:
  sudo:
    comment: |
      Abuse when chattr is allowed via sudo without restrictions.
    code: |
      sudo chattr +i /etc/passwd

  suid:
    comment: |
      Abuse when chattr binary has the SUID bit set.
    code: |
      ./chattr +i /etc/crontab
  
---
