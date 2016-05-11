#!/usr/bin/env python3
import os
import shutil

def copy(src, dest, mode=0o755):
    os.chmod(src, mode)
    shutil.copy(src, dest)


if __name__ == '__main__':
    distro = os.path.dirname(os.path.realpath(__file__))
    os.chdir(distro)

    config_dir = "/etc/hamachi-watchdog"
    install_dir = "/usr/share/hamachi-watchdog"
    systemd_dir = "/etc/systemd/system"

    os.makedirs(config_dir, mode=0o755, exist_ok=True)
    os.makedirs(install_dir, mode=0o755, exist_ok=True)

    copy("hamachi-watchdog.py", install_dir, mode=0o755)
    copy("hamachi-watchdog.conf", config_dir, mode=0o644)
    copy("hamachi-watchdog.service", systemd_dir, mode=0o644)
    copy("hamachi-watchdog.timer", systemd_dir, mode=0o644)
    copy("autorestartable-hamachi.service", systemd_dir, mode=0o644)

    os.system("systemctl daemon-reload")
    os.system("systemctl enable hamachi-watchdog.service")
    os.system("systemctl enable hamachi-watchdog.timer")
