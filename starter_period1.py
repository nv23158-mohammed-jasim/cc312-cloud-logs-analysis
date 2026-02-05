# starter_period1.py

total_lines = 0
invalid_lines = 0
invalid_level = 0

info_count = 0
warn_count = 0
error_count = 0

allowed_levels = {"INFO", "WARN", "ERROR"}

try:
    with open("logs.txt", "r") as file:
        for line in file:
            total_lines += 1
            line = line.strip()

            parts = line.split("|")

            # Check for exactly 4 fields
            if len(parts) != 4:
                invalid_lines += 1
                continue

            timestamp, level, service, message = parts
            level = level.strip().upper()

            # Check for valid level
            if level not in allowed_levels:
                invalid_level += 1
                continue

            # Count valid levels
            if level == "INFO":
                info_count += 1
            elif level == "WARN":
                warn_count += 1
            elif level == "ERROR":
                error_count += 1

except FileNotFoundError:
    print("logs.txt not found.")
    exit(1)

summary = (
    f"Total lines: {total_lines}\n"
    f"Invalid lines: {invalid_lines}\n"
    f"INFO: {info_count}\n"
    f"WARN: {warn_count}\n"
    f"ERROR: {error_count}\n"
    f"INVALID_LEVEL: {invalid_level}\n"
)

print(summary)

with open("period1_report.txt", "w") as report:
    report.write(summary)