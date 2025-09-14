import time
from collections import defaultdict

LOG_FILE = "sample.log"  # change to /var/log/auth.log on real Linux

failed_attempts = defaultdict(int)

def check_logs():
    with open(LOG_FILE, "r") as f:
        lines = f.readlines()
    for line in lines:
        if "Failed password" in line:
            parts = line.split()
            ip = parts[-4]
            failed_attempts[ip] += 1
            if failed_attempts[ip] > 3:
                print(f"⚠️ ALERT: {ip} failed {failed_attempts[ip]} times!")

print("🔎 Monitoring logs... (Ctrl+C to stop)")
while True:
    check_logs()
    time.sleep(5)  # check every 5 seconds
