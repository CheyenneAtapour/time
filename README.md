# An alternate representation of time

We keep the notion of seconds as our base unit. There are 86400 seconds in a full 24 hour day.  
We then create a unit of hundred-seconds, which is 100 seconds. Thus a day has 864 hundred-seconds.  
We further divide these hundred-seconds by 100, giving 8.64 "hundred-hours" in a day.  
We currently have two displays: one which shows time advancing by the second, and the other which only shows advancements on the hundred-second.

# To Run

python shy_time.py

# Notes

8 hours is 28,800 seconds, or 288 hundred-seconds.  
Noon (when PM begins) is 432 hundred-seconds, or 4:32.    
A day begins at 0:00 and Midnight is 8:64.
