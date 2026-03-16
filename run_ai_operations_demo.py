import subprocess
import os

print("Healthcare AI Operations Demo")
print("=============================")
print()

base_dir = os.path.dirname(os.path.abspath(__file__))

helpdesk_script = os.path.join(
    base_dir,
    "ai-helpdesk-automation",
    "scripts",
    "generate_helpdesk_report.py"
)

network_script = os.path.join(
    base_dir,
    "ai-network-incident-analysis",
    "scripts",
    "generate_incident_report.py"
)

print("Running Helpdesk Automation Report...")
print("--------------------------------------")
subprocess.run(["python", helpdesk_script], check=False)

print()
print("Running Network Incident Analysis Report...")
print("--------------------------------------------")
subprocess.run(["python", network_script], check=False)

print()
print("Demo complete.")
