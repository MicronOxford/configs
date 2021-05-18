Quick iunstructions on how to setup systemd on the Red Pitaya to
Autostart the cockpitDSP service at boot time.

IMD 20210518



1) Download the cockpitDSP github files from
https://github.com/MicronOxford/RedPitaya-DSP

2) the config expect the code to be in /root/RedPitaya-DSP so put it
there.

3) copy the startup script (start-DSP.sh) to /root/RedPitaya-DSP

4) copy the cockpit service definition (cockpitDSP.service) to
/etc/systemd/system

5) create a link to ensure it runs in multi user mode.

cd /etc/systemd/system/multi-user.target.wants
ln -s /etc/systemd/system/cockpitDSP.service .

6) finally start up the serviuec in systemd
 systemctl start cockpitDSP.service

you can check it is running by doing
systemctl status cockpitDSP.service
