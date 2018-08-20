---
  description: Read and write files limited to the current directory.
  file-write:
    - code: |
        red file_to_write
        a
        data
        .
        w
        q
  file-read:
    - code: |
        red file_to_read
        ,p
        q
---
