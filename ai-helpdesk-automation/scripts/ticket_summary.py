import csv
from collections import Counter

tickets = []

with open("../data/sample-tickets.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        tickets.append(row)

categories = Counter(ticket["category"] for ticket in tickets)

print("Helpdesk Ticket Category Summary")
print("--------------------------------")

for category, count in categories.items():
    print(f"{category}: {count} tickets")
