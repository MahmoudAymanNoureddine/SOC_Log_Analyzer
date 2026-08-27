file = open("sample_log.txt", "r")

logs = file.readlines()

file.close()

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

total_events = failed + success + warnings + errors

print("\nSOC Security Report")
print("=" * 30)

print("Failed Logins     :", failed)
print("Successful Logins :", success)
print("Warnings          :", warnings)
print("Errors            :", errors)
if failed >= 5:
    print("Risk Level : HIGH")

elif failed >= 3:
    print("Risk Level : MEDIUM")

else:
    print("Risk Level : LOW")

print("-" * 30)
print("Total Events      :", total_events)

if failed >= 5:
    print("\nALERT: High number of failed login attempts detected!")

if errors >= 3:
    print("ALERT: Multiple system errors detected!")
