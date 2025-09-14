# parser.py - Detect brute force attempts from logs

from collections import defaultdict

# read log file
with open("sample.log", "r") as f:
    logs = f.readlines()

failed_attempts = defaultdict(int)

# scan logs
for line in logs:
    if "Failed password" in line:
        parts = line.split()
        ip = parts[-4]  # get the IP address
        failed_attempts[ip] += 1

# show results
print("=== Failed login attempts by IP ===")
for ip, count in failed_attempts.items():
    print(f"{ip}: {count} times")

# alert if IP tried more than 3 times
print("\n=== Potential brute force attacks ===")
for ip, count in failed_attempts.items():
    if count > 3:
        print(f"⚠️ ALERT: {ip} failed {count} times!")
