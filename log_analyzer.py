def analyze_logs(filename):

    try:

        file = open(filename, "r")

        logs = file.readlines()

        file.close()

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

        print("\nSOC SECURITY REPORT")
        print("=" * 40)

        print(f"Failed Logins      : {failed}")
        print(f"Successful Logins  : {success}")
        print(f"Warnings           : {warnings}")
        print(f"Errors             : {errors}")

        print("-" * 40)
        print(f"Total Events       : {total_events}")

        print("-" * 40)

        if failed >= 5 or errors >= 3:
            risk_level = "HIGH"

        elif failed >= 3 or errors >= 1:
            risk_level = "MEDIUM"

        else:
            risk_level = "LOW"

        print(f"Risk Level         : {risk_level}")

        print("-" * 40)

        if failed >= 5:
            print("ALERT: Possible Brute Force Attack Detected")

        if errors >= 3:
            print("ALERT: Multiple System Errors Detected")

        if warnings >= 3:
            print("ALERT: Unusual Warning Activity Detected")

    except FileNotFoundError:

        print("Error: Log file not found.")

    except Exception as error:

        print("Unexpected Error:", error)


analyze_logs("sample_log.txt")
