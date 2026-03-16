import csv
from collections import Counter

alerts = []

with open("../data/network-alerts.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        alerts.append(row)

alert_types = Counter(alert["alert_type"] for alert in alerts)
severity_levels = Counter(alert["severity"] for alert in alerts)

total_alerts = len(alerts)
most_common_alert = alert_types.most_common(1)[0][0]
highest_severity = severity_levels.most_common(1)[0][0]

print("AI-Style Incident Report")
print("========================")
print(f"Total alerts analyzed: {total_alerts}")
print(f"Most common alert type: {most_common_alert}")
print(f"Most frequent severity level: {highest_severity}")
print()

print("Alert Type Breakdown:")
for alert_type, count in alert_types.items():
    print(f"- {alert_type}: {count}")

print()
print("Severity Breakdown:")
for severity, count in severity_levels.items():
    print(f"- {severity}: {count}")

print()
print("Operational Summary:")
print(
    "This fictional dataset suggests recurring infrastructure issues that may require network engineering review. "
    "AI-assisted analysis can help identify common alert patterns, summarize severity trends, and support faster troubleshooting."
)
