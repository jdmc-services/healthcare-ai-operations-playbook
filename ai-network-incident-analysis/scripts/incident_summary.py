import csv
from collections import Counter

alerts = []

with open("../data/network-alerts.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        alerts.append(row)

alert_types = Counter(alert["alert_type"] for alert in alerts)
severity_levels = Counter(alert["severity"] for alert in alerts)

print("Network Alert Type Summary")
print("--------------------------")

for alert_type, count in alert_types.items():
    print(f"{alert_type}: {count}")

print("\nSeverity Summary")
print("----------------")

for severity, count in severity_levels.items():
    print(f"{severity}: {count}")
