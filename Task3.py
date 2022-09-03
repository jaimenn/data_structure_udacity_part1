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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

## Part A

area_codes_by_bang = set()  # list of codes called by Bangalore

for call in calls:
    if call[0][:5] == "(080)":  # if calling number from Bangalore

        if call[1][1] == "0":  # add fixed line area codes between parentheses
            for i, v in enumerate(call[1]):
                if v == ")":
                    area_codes_by_bang.add(call[1][:i + 1])

        elif " " in call[1]:  # add mobile codes
            area_codes_by_bang.add(call[1][:4])

        elif call[1][:3] == "140":  # add Telemarketers code
            area_codes_by_bang.add("140")

code_list = sorted(list(area_codes_by_bang))  # convert to list and sort

# print codes line by line
print("The numbers called by people in Bangalore have codes:")
for code in code_list:
    print(code)

## Part B

calls_bang_to_bang = 0  # count of calls from Bangalore to Bangalore,
calls_bang_to_any = 0  # count of calls from Bangalore to anywhere

for call in calls:

    if call[0][:5] == "(080)":  # calls from Bangalore

        if call[1][:5] == "(080)":  # calls to Bangalore
            calls_bang_to_bang += 1  # increase count of calls from bang to bang
            calls_bang_to_any += 1  # and count of any calls

        else:
            calls_bang_to_any += 1  # increase ony count of any calls

percentage = (calls_bang_to_bang / calls_bang_to_any) * 100

message = "{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."

print(message.format("%.2f" % percentage))