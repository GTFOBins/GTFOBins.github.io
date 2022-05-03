---
description: This programm is used to display some system info along with a chosen image in a terminal window.
functions:
  file-read:
    - description: The file content is used as the logo while some other information is displayed on its right, thus it might not be suitable to read arbitray binary files.
      code: |
        LFILE=file_to_read
        neofetch --ascii $LFILE

  command:
    - description: The programm innerly reads its config file from a predefined path or from a file specified by an option. Then it does `CONFIG_FILE=/path/to/config.conf source $CONFIG_FILE`. So, it's possible to execute arbitrary commands if the contents of the config file is controlled by an attacker.
      code: |
        echo 'bash' > config.conf # desired command
				CONFIG_FILE=config.conf
        neofetch --config $CONFIG_FILE
---
