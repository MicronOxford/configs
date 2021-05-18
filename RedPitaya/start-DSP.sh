#!/bin/bash
#short script to enable start of the DSP server from systemd
#IMD 2020/09/08
#

(cd /root/RedPitaya-DSP ; /usr/local/bin/python3 src/server.py 2>&1 >> DSP-server.log)

