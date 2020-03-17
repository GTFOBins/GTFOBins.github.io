---
functions:
  shell:
    - code: |
        pry
        system("/bin/sh")
  sudo:
    - code: |
        sudo pry
        system("/bin/sh")
  limited-suid:
    - code: |
        ./pry
        system("/bin/sh")
---
