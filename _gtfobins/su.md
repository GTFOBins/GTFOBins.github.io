---
description: This can be used to impersonate other users, as long as you have their password. When run with `sudo`, the other user's password isn't needed.
functions:
  shell:
    - description: Launches a shell as the specified user
	  code: |
	    su [user]
  suid:
    - description: The SUID bit is set, which means any user on the system can be impersonated, since root permissions to do so.
	  code: |
		su [user]
  sudo:
    - description: Since root can impersonate anyone on the system, no password is needed to impersonate any user on the system (beyond the password to use `sudo` itself, if required).
	  code: |
		sudo su [user]
---
