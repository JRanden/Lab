import subprocess

ipAddresses = ["127.0.0.1", "192.168.116.2", "10.0.0.3", "google.com", "vg.no"]
onlineHosts = []
offlineHosts = []

def checkPing(): 
    for ip in ipAddresses:
        try:
            subprocess.run(["ping", "-c", "1", ip], capture_output=True, check=True, timeout=2)
            onlineHosts.append(ip)
            print(f"{ip} er online")
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError):
            offlineHosts.append(ip)
            print(f"{ip} er offline")

checkPing()
print("Online:", onlineHosts)
print("Offline:", offlineHosts)