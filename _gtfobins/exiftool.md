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
