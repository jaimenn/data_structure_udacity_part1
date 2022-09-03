"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from collections import defaultdict

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

time_spent_dict = defaultdict(int)

for call in calls:
    # add outgoing number time to number key
    time_spent_dict[call[0]] += int(call[3])

    # add receiving number time to number key
    time_spent_dict[call[1]] += int(call[3])

# identify the longest time value
longest_time = max(time_spent_dict.values())

# identify the number spent longest time
for number, time in time_spent_dict.items():
    if time == longest_time:
        # print the message
        print("{} spent longest time, {} seconds, on the phone during September 2016.".format(number, time))