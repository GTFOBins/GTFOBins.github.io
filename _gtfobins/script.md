---
functions:
  shell:
    - code: script -q /dev/null
  sudo:
    - code: sudo script -q /dev/null
  file-write:
    - description: The wrote content is corrupted by debug prints.
      code: script -q -c 'echo DATA' file_to_write
---
