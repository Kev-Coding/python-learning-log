instrument_tags = ['FT-101', 'TT-303', 'PT-404', 'LIT-501']   

for tag in instrument_tags:
    # Check the type of instrument
    if tag.startswith('FT'):
        print(f"Flow Sensor Detected: {tag}")
    else:
        print(f"Processing instrument tag: {tag}")


temperature = 30
while temperature < 50:
    print(f"Current temperature: {temperature}°C")
    temperature += 1.5
print("Target temperature reached.")
