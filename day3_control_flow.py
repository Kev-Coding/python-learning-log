# Todays lesson is if/elif/else
# is_pump_on = True
# if is_pump_on:
#     print("Pump is ON")
# else:
#     print("Pump is OFF")

temperature = 99
pressure = 33
is_active = True

if temperature > 100:
    print("Warning: Temperature exceeds safe limits!")
elif temperature > 32:
    print("Temperature is within safe limits.")
else:
    print("Warning: Temperature is below freezing.")


# and/or/not f statements
if pressure > 50 or temperature > 100:
    print("Pump WARNING!")
else:
     print("Pump is normal.")

# Nested if statements
if is_active:
    print("System is active.")
    if temperature > 100:
        print("Warning: High temperature detected!")
    else:
        print("Temperature is normal.")