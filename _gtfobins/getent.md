---
description: |
  `getent` is a utility that retrieves entries from administrative databases configured 
  via the Name Service Switch (NSS). If misconfigured with the SUID bit, it can be abused 
  to access sensitive databases such as `shadow`, which contains user password hashes, 
  including root's.

  This can lead to local privilege escalation by leaking password hashes for offline cracking.

functions:
  suid:
    - code: |
        # Leak root hash from /etc/shadow via getent SUID binary
        ./getent shadow root
    - code: |
        # Dump all hashes
        ./getent shadow
---
