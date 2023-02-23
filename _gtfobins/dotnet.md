---
functions:
  shell:
    - code: |
        dotnet fsi
        System.Diagnostics.Process.Start("/bin/sh").WaitForExit();;
  file-read:
    - code: |
        export LFILE=file_to_read
        dotnet fsi
        System.IO.File.ReadAllText(System.Environment.GetEnvironmentVariable("LFILE"));;
  sudo:
    - code: |
        sudo dotnet fsi
        System.Diagnostics.Process.Start("/bin/sh").WaitForExit();;
---
