from datetime import datetime


def analyze_logs(filename):

    try:

        with open(filename, "r") as file:
            logs = file.readlines()

        failed = 0
        success = 0
        warnings = 0
        errors = 0

        for line in logs:

            line = line.strip()

            if "Failed Login" in line:
                failed += 1

            elif "Successful Login" in line:
                success += 1

            elif "Warning" in line:
                warnings += 1

            elif "Error" in line:
                errors += 1

        total_events = failed + success + warnings + errors

        if failed >= 5 or errors >= 3:
            risk_level = "HIGH"

        elif failed >= 3 or errors >= 1:
            risk_level = "MEDIUM"

        else:
            risk_level = "LOW"

        current_time = datetime.now()

        print("\nSOC SECURITY REPORT")
        print("=" * 50)

        print("Analysis Time      :", current_time)

        print("=" * 50)

        print("Failed Logins      :", failed)
        print("Successful Logins  :", success)
        print("Warnings           :", warnings)
        print("Errors             :", errors)

        print("-" * 50)

        print("Total Events       :", total_events)

        print("-" * 50)

        print("Risk Level         :", risk_level)

        print("-" * 50)

        if risk_level == "HIGH":
            print("Recommendation     : Immediate Investigation Required")

        elif risk_level == "MEDIUM":
            print("Recommendation     : Review Security Logs")

        else:
            print("Recommendation     : Continue Monitoring")

        print("-" * 50)

        if failed >= 5:
            print("ALERT: Possible Brute Force Attack Detected")

        if errors >= 3:
            print("ALERT: Multiple System Errors Detected")

        if warnings >= 3:
            print("ALERT: Unusual Warning Activity Detected")

        print("=" * 50)

    except FileNotFoundError:

        print("ERROR: Log file not found.")

    except Exception as error:

        print("Unexpected Error:", error)


analyze_logs("sample_log.txt")
