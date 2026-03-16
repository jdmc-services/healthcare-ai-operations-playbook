import csv
from collections import Counter

tickets = []

with open("../data/sample-tickets.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        tickets.append(row)

categories = Counter(ticket["category"] for ticket in tickets)
priorities = Counter(ticket["priority"] for ticket in tickets)

total_tickets = len(tickets)
most_common_category = categories.most_common(1)[0][0]
most_common_priority = priorities.most_common(1)[0][0]

print("AI Helpdesk Operational Report")
print("==============================")
print(f"Total tickets analyzed: {total_tickets}")
print(f"Most common issue category: {most_common_category}")
print(f"Most frequent priority level: {most_common_priority}")
print()

print("Ticket Category Breakdown:")
for category, count in categories.items():
    print(f"- {category}: {count}")

print()
print("Priority Breakdown:")
for priority, count in priorities.items():
    print(f"- {priority}: {count}")

print()
print("Operational Summary:")
print(
    "The fictional dataset suggests recurring support issues that could benefit from automation or knowledge base improvements. "
    "AI-assisted analysis can help support teams identify recurring problems, prioritize high-impact incidents, "
    "and recommend troubleshooting steps more quickly."
)
