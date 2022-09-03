"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

nums_make_out_calls = set() # numbers make outgong calls
nums_recieve_calls = set() # numbers recieve incoming calls
nums_send_texts = set() # numbers send texts
nums_recieve_texts = set() # numbers recieve texts

for call in calls:
	nums_make_out_calls.add(call[0])
	nums_recieve_calls.add(call[1])


for text in texts:
	nums_send_texts.add(text[0])
	nums_recieve_texts.add(text[1])


telemarketers = sorted(list(nums_make_out_calls - (nums_recieve_calls | nums_send_texts | nums_recieve_texts)))
print("These numbers could be telemarketers: ")
for telemarketer in telemarketers:
	print(telemarketer)
