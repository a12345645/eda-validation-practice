import re
import os

def parse_log(file_path):
    result = {
        "design": os.path.basename(file_path).replace(".log", ""),
        "cell_count": None,
        "area": None,
        "slack": None
    }

    with open(file_path) as f:
        for line in f:
            if "Number of cells" in line:
                result["cell_count"] = int(re.search(r"\d+", line).group())
            elif "Area" in line:
                result["area"] = float(re.search(r"[\d.]+", line).group())
            elif "Slack" in line:
                result["slack"] = float(re.search(r"[-\d.]+", line).group())

    return result

# Parse all logs
log_dir = "logs"
results = []
for filename in os.listdir(log_dir):
    if filename.endswith(".log"):
        parsed = parse_log(os.path.join(log_dir, filename))
        results.append(parsed)

# Print or write to CSV
import csv
with open("reports/summary.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["design", "cell_count", "area", "slack"])
    writer.writeheader()
    writer.writerows(results)
