---
description: Bzip2 is used to compress and decompress files.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
	bzip2 -z "$LFILE"
	bzip2 -d -c "$LFILE.bz2"
  suid:
    - code: |
        LFILE=file_to_read
        ./bzip2 -z "$LFILE"
	./bzip2 -d -c "$LFILE.bz2"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo bzip2 -z "$LFILE"
	sudo bzip2 -d -c "$LFILE.bz2"
---
