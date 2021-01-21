---
functions:
  sudo:
    - description: The command execution is blind (displayed on the virtual console), but it is possible to save the output on a temporary file.
      code: |
        COMMAND=id
        TF=$(mktemp -u)
        sudo openvt -- sh -c "$COMMAND >$TF 2>&1"
        cat $TF
---
