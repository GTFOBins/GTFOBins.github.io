---
description: Read and write files limited to the current directory.
functions:
  file-write:
    - code: |
        red file_to_write
        a
        DATA
        .
        w
        q
  file-read:
    - code: |
        red file_to_read
        ,p
        q
---
