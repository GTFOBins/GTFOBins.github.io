---
functions:
  execute-non-interactive:
  - description: The commands are executed according to the crontab file edited via the `crontab` utility.
    code: crontab -e
  sudo-enabled:
  - description: The commands are executed according to the crontab file edited via the `crontab` utility.
    code: sudo crontab -e
---
