import random
def check_temp_status(temp):
     """
    Checks the temperature and prints a status message based on a given value.
    This function demonstrates conditional logic.
    """
    if temp >100:
         print(f"Alert: High temperature detected! ({temp}°C)")
    elif temp > 30:
         print(f"Temperature is in the normal range. ({temp}°C)")
    else:
        print(f"Alert: Low temperature detected! ({temp}°C)")

check_temp_status(random.randint(0, 120))

