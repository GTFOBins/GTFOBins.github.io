---
description: Utility to Secure Delete a File in Unix
functions:
  - name: Execute arbitrary commands as root
    platform: unix
    exploit:
      - "If shred is run as root, you can abuse it to execute arbitrary commands by deleting files or scripts:"
      - "`shred -u /path/to/important/file`"
      - "For example, if you control the file `/tmp/myscript.sh`, you could shred it to trigger deletion and combine it with other root permissions to escalate."
  - name: Delete arbitrary files
    platform: unix
    exploit:
      - "`shred -u /path/to/file` deletes the specified file securely."
      - "When run as root, any file on the system can be securely deleted using this command."
notes:
  - "Requires the shred binary to be run with elevated privileges (root)."
  - "Abuse potential depends on system configuration and file permissions."
  - "This is primarily a file deletion vector, not arbitrary code execution, unless combined with other exploits."
---
