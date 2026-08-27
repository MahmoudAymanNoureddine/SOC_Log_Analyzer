file = open("sample_log.txt", "r")

logs = file.readlines()

failed = 0
success = 0
warnings = 0
errors = 0

for line in logs:

    if "Failed Login" in line:
        failed += 1

    elif "Successful Login" in line:
        success += 1

    elif "Warning" in line:
        warnings += 1

    elif "Error" in line:
        errors += 1

print("SOC Report")
print("-------------------")
print("Failed Logins :", failed)
print("Successful Logins :", success)
print("Warnings :", warnings)
print("Errors :", errors)
