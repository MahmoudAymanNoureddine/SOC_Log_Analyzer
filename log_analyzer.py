def analyze_log(file_name):

    failed_logins = 0
    successful_logins = 0
    warnings = 0
    errors = 0

    try:
        with open(file_name, "r") as file:

            for line in file:

                line = line.strip()

                if line == "FAILED_LOGIN":
                    failed_logins += 1

                elif line == "SUCCESS_LOGIN":
                    successful_logins += 1

                elif line == "WARNING":
                    warnings += 1

                elif line == "ERROR":
                    errors += 1

        print("\n========== SOC REPORT ==========")

        print(f"Failed Logins : {failed_logins}")
        print(f"Success Logins: {successful_logins}")
        print(f"Warnings      : {warnings}")
        print(f"Errors        : {errors}")

    except FileNotFoundError:
        print("Log file not found.")


analyze_log("sample_log.txt")
