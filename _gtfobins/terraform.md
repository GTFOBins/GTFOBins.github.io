---
description: Terraform is an open-source infrastructure-as-code software tool created by HashiCorp.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        echo 'file("'$LFILE'")' | terraform console
  sudo:
    - code: |
        LFILE=file_to_read
        echo 'file("'$LFILE'")' | sudo terraform console
---
