---
functions:
  shell:
    - code: pwsh
  file-write:
    - code: |
        export LFILE=file_to_write
        pwsh -c '"DATA" | Out-File $env:LFILE'
  sudo:
    - code: sudo pwsh
---
