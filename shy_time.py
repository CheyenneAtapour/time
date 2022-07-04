import os
import time
import datetime

prev_seconds = datetime.datetime.now().second

while True:
	time = datetime.datetime.now()
	if time.second == prev_seconds:
		continue

	seconds = (time.hour * 60 * 60) + (time.minute * 60) + time.second
	prev_seconds = time.second
	os.system('cls' if os.name == 'nt' else 'clear')
	print("{:.2f}".format(seconds / 100) + " / 864")
	dec_seconds = int(seconds / 100) / 100
	print("{:.2f}".format(dec_seconds).replace(".", ":")) 
	#print("\n(Day ends at 864)")
