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


print("\n========== SOC REPORT ==========")

print("Failed Logins :", failed)
print("Successful Logins :", success)
print("Warnings :", warnings)
print("Errors :", errors)

print("\n========== RISK ANALYSIS ==========")

if failed >= 5:
    print("Risk Level : HIGH")

elif failed >= 3:
    print("Risk Level : MEDIUM")

else:
    print("Risk Level : LOW")


file.close()
