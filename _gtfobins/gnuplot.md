---
functions:
  sudo:
    - code: |
        COMMAND=id
        sudo gnuplot -e 'set print "-" ; print system("'$COMMAND'")'
  file-read:
    - code: |
        LFILE=file_to_read
        sudo gnuplot -e 'set print "-" ; print system("cat '$LFILE'")'
---
