# Todays lesson is if/elif/else
is_pump_on = True
if is_pump_on:
    print("Pump is ON")
else:
    print("Pump is OFF")

temperature = 33
if temperature > 100:
    print("Warning: Temperature exceeds safe limits!")
elif temperature > 32:
    print("Temperature is within safe limits.")
else:
    print("Warning: Temperature is below freezing.")