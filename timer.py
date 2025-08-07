# time.py

import time # Used to create the countdown delay
from datetime import datetime, timedelta # Used to calculate end time

# Ask the user how long the want to focus (in minutes)
minutes = input("⏳ How many minutes would you like to focus for? ")

# Validate input to ensure it's a positive number
try:
	minutes = int(minutes)
	if minutes <= 0:
		raise ValueError
except ValueError:
	print("❌ Please enter a valid number greater than 0.")
	exit()

# Calculate total seconds for countdown
total_seconds = minutes * 60

# Calculate the end time
end_time = datetime.now() + timedelta(seconds=total_seconds)

print(f"🔔 Timer started for {minutes} minutes. Focus until {end_time.strftime('%H:%M:%S')}")

# Countdown loop
while total_seconds:
	mins, secs = divmod(total_seconds, 60) # Break seconds into minutes and seconds
	timer_display = f"{mins:02d}:{secs:02d}" # Format time as MM:SS
	print(f"\r⏰ Time left: {timer_display}", end="") # Print on the same line
	time.sleep(1) # Wait for 1 second
	total_seconds -= 1 # Subtract one second

# Notify the user when time is up
print("\n✅ Time's up! Take a short break or start another session.")










