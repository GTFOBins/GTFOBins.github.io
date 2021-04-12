---
functions:
  file-read:
    - code: zsh -c "echo $(</file/to/read.txt)"
  file-write:
    - code: zsh -c 'echo DATA > /file/to/write.txt'
  shell:
    - code: zsh
  suid:
    - code: ./zsh
  sudo:
    - code: sudo zsh
---
