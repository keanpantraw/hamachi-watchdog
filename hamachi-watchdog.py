#!/usr/bin/env python3
import json
import os
import subprocess


def connection_lost(network_id, timeout_seconds):
    p = subprocess.Popen(["hamachi", "go-online", network_id])
    try:
        p.wait(timeout_seconds)
    except subprocess.TimeoutExpired:
        p.kill()
        return True
    return False


if __name__ == "__main__":
    with open("/etc/hamachi-watchdog/hamachi-watchdog.conf", "r") as f:
        config = json.load(f)
        network_id = config['network_id']
        timeout_seconds = config['timeout_seconds']
    if connection_lost(network_id, timeout_seconds):
        print("Hamachi looks down. Restarting it...")
        os.system("systemctl restart logmein-hamachi.service")
        print("Hamachi was restarted")
