This is watchdog which automatically restarts logmein-hamachi service
when for some reason connection to given VPN was lost.

Execute install.py under root to install it.
Specify your network id (numeric one, name doesn't count) in config file after installation.
Launch watchdog using:

``systemctl start hamachi-watchdog.timer``


Requires:
---------

* python3.4+
* systemd
