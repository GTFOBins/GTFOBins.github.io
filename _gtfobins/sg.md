---
functions:
  shell:
    - description: Commands can be run if the current user's group is specified, therefore no additional permissions are needed.
      code: |
        sg $(id -ng)
  sudo:
    - code: |
        sudo sg root
---
