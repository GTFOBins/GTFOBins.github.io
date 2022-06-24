---
functions:
  file-upload:
    - description: create HTTP server to upload files from a directory
      code: kubectl proxy --address=0.0.0.0 --www=/tmp/ --www-prefix=/tmp/
---
