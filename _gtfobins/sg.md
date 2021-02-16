---
functions:
  shell:
    - description: Commands can be run if the current user's group is specified, therefore no additional permissions are needed.
      code: |
        GROUPNAME=users
        sg $GROUPNAME -c "/bin/sh"
  command:
    - description: Commands can be run if the current user's group is specified, therefore no additional permissions are needed.
      code: |
        COMMAND=whoami
        GROUPNAME=users
        sg $GROUPNAME -c $COMMAND
  sudo:
    - description: Any group can be specified as the user will have root permissions.
      code: |
        GROUPNAME=users
        sudo sg $GROUPNAME -c "/bin/sh"
---
