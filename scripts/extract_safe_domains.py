#!/usr/bin/env python3

import requests
import re
import datetime
from collections import Counter

# Loki configuration
LOKI_URL = "http://GrafanaLoki:3100/loki/api/v1/query_range"
CONTAINER_NAME = "binhex-official-pihole"

# Query range (past 30 days)
now = int(datetime.datetime.now().timestamp())
start = now - (30 * 24 * 60 * 60)

# LogQL query: extract successful DNS replies
query = '{container_name="%s"} |~ "reply .* is .*"' % CONTAINER_NAME

print("[🔍] Querying Loki for DNS replies...")
resp = requests.get(LOKI_URL, params={
    "query": query,
    "start": start * 1_000_000_000,
    "end": now * 1_000_000_000,
    "limit": 5000,
    "direction": "BACKWARD"
})

data = resp.json()

# Extract domains from logs
pattern = re.compile(r'reply\s+([a-zA-Z0-9.-]+)\s+is')
domains = []

for stream in data.get("data", {}).get("result", []):
    for entry in stream.get("values", []):
        logline = entry[1]
        match = pattern.search(logline)
        if match:
            domains.append(match.group(1).lower())

print(f"[📦] Found {len(domains)} domains in logs")

# Count frequencies
domain_counts = Counter(domains)

# Load existing whitelist
with open("whitelist.txt", "r") as f:
    existing = set()
    for line in f:
        clean = line.strip().split("#")[0].strip()
        if clean:
            existing.add(clean)

# Basic denylist to avoid known bad entries (expand this as needed)
denylist = {
    "doubleclick.net", "googlesyndication.com", "ads.example.com"
}

# Filter new safe domains (appear multiple times, not in whitelist or denylist)
suggested = [
    domain for domain, count in domain_counts.items()
    if count > 5 and domain not in existing and domain not in denylist
]

# Sort and append to whitelist
if suggested:
    print(f"[🧠] Suggesting {len(suggested)} new domains...")
    with open("whitelist.txt", "a") as f:
        f.write("\n\n# 🌱 Suggested domains from logs ({}):\n".format(datetime.date.today()))
        for domain in sorted(suggested):
            f.write(f"{domain}  # Auto-suggested from logs\n")
else:
    print("[✅] No new safe domains to suggest this run.")
