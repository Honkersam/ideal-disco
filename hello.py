# Import time for pauses
import time
# Import random for randomness
import random as rnd
# Import math for extra math-ness
import math
# Import datetime for head breaking date and time formatting
import datetime as dt
# Import timezone stuff for even more head breaaking (hopefully it isn't broken)
# Why is dateutil so thik you need .tz and why is tz so thik we need to get only gettz?
from dateutil.tz import gettz

print(rnd.randint(0,9))
# time.sleep(3)
# why I left this in the file for this long, I will never know.
# this tiny pause was finally commented 5 months and one day after this document was created
# creation: Tue 24 Sep 2024 08:03:25 PM
# finally commented: Tue 25 Feb 2025 09:47:33 PM 
print(rnd.randint(4,7))

# This is a comment bruv.
"""Now, this is a 
multiline comment wow! It is also called a 'Docstring,' but not many people
use that name"""

# You can use backslashes (\) to skip the quotes so they don't mess with the string
print('Mary\'s dog said "Woof".')
print("Mary's dog said\"Woof\".")

"""GOING OVER CONCEPTS I ALREADY KNOW, BUT IT'S NOT A BAD THING TO REVISIT THEM"""

# This variable contains an integer
quantity = 10
# This variable contains a float
unit_price = 1.99
# This variable contains the result of multiplying 'quantity' times 'unit price'
extended_price = quantity * unit_price
# Show the results
print(extended_price)

# This variable contains an integer
quantity = 14
# This variable contains a float
unit_price = 26.99
# This variable contains the result of multiplying 'quantity' times 'unit price'
extended_price = quantity * unit_price
# Show some results on the screen
print(extended_price)

# MATH
pi = 3.14159265358979
x = 128
y = -345.67890987
z = -999.9999
# Absolute value (positive only), chops off the "-" sign on negatives
print(abs(z))
# Integer (cuts off all decimals)
print(int(z))
# Combo
print(int(abs(z)))
# Round x (pi) to y (4) digits
print(round(pi, 4))
# Convert x to binary (shown as 0b#)
print(bin(x))
# Covert x to hexadecimal (shown as 0x#)
print(hex(x))
# Convert x to an octal number (shown as 0o#)
print(oct(x))
# Return the max number in the set of data
print(max(pi, x, y, z))
# Return the min number in the set of data
print(min(pi, x, y, z))
# Returns the data type of x (pi) as a string
print(type(pi))
# Returns the data type of x as a string
print(type(x))
# Returns the data type of x (y) as a string after converting to a string
print(type(str(y)))

pi = math.pi
e = math.e
tau = math.tau
x = 81
y = 7
z = -23234.5454
print(pi)
print(e)
print(tau)
# Square root
print(math.sqrt(x))
# Factorial (10!)
print(math.factorial(y))
# Round down to the nearest integer (floor)
print(math.floor(z))
# Round up to the nearest integer (ceiling)
print(math.ceil(z))
# Convert radians to degrees
print(math.degrees(y))
# Convert degrees to radians
print(math.radians(45))

"""Okay, we getting into the real meat now. Formatting with f-strings!"""

# Anything in the curly brackets is the expression the f operates on
username = "Alan"
print(f"Hello {username}")

# Can stick things together
unit_price = 49.99
quantity = 30
# Sticks the dollar sign to the result
print(f"Subtotal: ${quantity * unit_price}")
# That number looks ugly like that, so we can add :, after the contents to put a comma in the thousand's place
print(f"Subtotal: ${quantity * unit_price:,}")
# We can also add .2f to fix the decimals at 2 places
print(f"Subtotal: ${quantity * unit_price:,.2f}")

# Percents can also be formatted
# Make sure to write precents as a float (underneath is 6.5%)
sales_tax_rate = 0.065
print(f"Sales tax rate {sales_tax_rate}")
# Slap on .2% to format it into a percent with 2 decimal places. Don't forget the :!
print(f"Sales Tax Rate {sales_tax_rate:.2%}")

# Cool, right? But, we can go one step further, and actually align numbers!
unit_price = 49.95
quantity = 32
sales_tax_rate = 0.065
subtotal = quantity * unit_price
sales_tax = sales_tax_rate * subtotal
total = subtotal + sales_tax
output = f'''
Subtotal:  ${subtotal:.2f}
Sales Tax: ${sales_tax:.2f}
Total:     ${total:.2f}
'''
print(output)

# The numbers are all over the place, but we can align them all to 9 digits with >9 after the :!
# :> aligns to the right
# :< aligns to the left
output = f'''
Subtotal:  ${subtotal:>9.2f}
Sales Tax: ${sales_tax:>9.2f}
Total:     ${total:>9.2f}
'''
print(output)

# The dollar signs aren't aligned, but we can do a little magic to remedy that
s_subtotal = "$" + f"{subtotal:.2f}"
s_sales_tax = "$" + f"{sales_tax:.2f}"
s_total = "$" + f"{total:.2f}" 
output = f'''
Subtotal:   {s_subtotal:>9}
Sales Tax:  {s_sales_tax:>9}
Total:      {s_total:>9}
'''
print(output)
# I know, very wonk, but it works!

# Tiny weird number break
x = 255
print(bin(x))
print(oct(x))
print(hex(x))
print(0b11111111)
print(0o377)
print(0xff)
# Brain Hurty
# complex(real, imaginary)
z = complex(2, -3)
print(z)
print(z.real)
print(z.imag)

# Getting the length of a string using len()
s1 = ""
s2 = " "
s3 = "A B C"
print(len(s1))
print(len(s2))
print(len(s3))

"""String Operator Time!"""
s = "Abracadabra Hocus Pocus you're a turtle dove"
# Is there a lowercase 't' in s?
print("t" in s)
# Is there no uppercase 'T' in s?
print("T" not in s)
# Print 15 hyphens in a row
print("-" * 15)
# Print the first character in string s
print(s[0])
# Print characters 33 - 39 from string s
print(s[33:39])
# Print every third character in s starting from 0
print(s[0:44:3])
# Print the lowest character in s (according to the ASCII chart)
print(min(s))
# Print the highest character in s (according to the ASCII chart)
print(max(s))
# Where is the first uppercase 'P'?
print(s.index("P"))
# Where is the first lowercase 'o' in the latter part of s?
# Note the returned value still starts at 0 (25 would be the 26th letter still)
print(s.index("o", 22, 44))
# How many lowercase letter 'a's are in string s?
print(s.count("a"))
# Print the ASCII character 127 (⌂ (alt + 127))
print(chr(127))

"""String nice-to-knows"""
string = "Hello World"
# The brackets allow us to do the list thing on a string
print(string[0])
print(string[4])
# Know this for everything, i : i is a range
print(string[2 : 7])
# .replace(string, string)
print(string.replace(s[0], ")
# KNOW THIS THOUROUGLY
# [n:r] returns the string starting at 0 + n, until 0 + r
# [-n:-r] returns the string starting at end - n, until end -r
# [x:] x is what to not include before x starting at 0, -x is starting from the end
# [:y] y is what to not include after y starting from 0, -y is starting from end
# [1:] returns the rest of the string, starting at that index
print(string[1:])
# [-1:] returns the rest of the string, starting from the end minus that number
print(string[-1:])
# [:-1] returns the string, up until that number before the end
print(string[:-1])
# [:1] only returns the first n letters of the string
print(string[:1])

"""Manipulating Strings With Methods"""
s1 = "There is no such word as schmeedledorp"
s2 = "   a b c    "
s3 = "ABC"
# Capitalize the first letter, rest lowercase
print(s3.capitalize())
# Count the number of spaces (" ") is s1
print(s1.count(" "))
# Find the first "e" in s1
print(s1.find("e"))
# Is s2 all lowercase?
print(s2.islower())
# Print s3 as all lowercase
print(s3.lower())
# Remove all leading spaces from s2
print(s2.lstrip())
# Remove all leading and trailing spaces from s2
print(s2.strip())
# Swap the case of s1 (upper to lower, and lower to upper)
print(s1.swapcase())
# Print s1 in title case (all first letters are upper and rest is lower)
print(s1.title())
# Print s1 as all uppercase
print(s1.upper())

"""So, uh, datetime. This is the section that is entirely dedicated to complex fromatting, 
just to show a damn date. Really, I don't know why anyone came up with this, 
and made it this annoying just to display the date.
Prepare to die."""
# dt.date()  Date consisting of the month, day, and year
# dt.time()  Time consisting of the hour, minute, second, and microsecond, but can optionally include time zone information
# dt.datetime()  Literally just date() and time() smooshed into one long string

"""Some goofy stuff that kinda resembles Java"""
# Get today's date using .today
today = dt.date.today()
# Now store a date using the datetime format
last_of_teens = dt.date(2019, 12, 31)
# Show the contents
print(today)
print(last_of_teens)
# You can isolate different parts of the date using .month, .day, or .year
# I will be so tempted to put () after it
print(last_of_teens.month)
print(last_of_teens.day)
print(last_of_teens.year)

"""Now we have a bunch of time and date information, we need proper formatting to display it. Yay."""

# Remember to check the book or online to find what each stupid % thing means

# %a weekday, abbreviated (Sun)
# %A weekday, full (Sunday)
# %b month, abbreviated (Jan)
# %B month, full (January)
# %m month, number 01 - 12 (07)
# %d day of the month, 01 - 31 (27)
# %y year, without century (24)
# %Y year, with century (2024)
print(f"{last_of_teens:%A, %B %d, %Y}") # Tuesday, December 31, 2019
# mm/dd/yyyy format
todays_date = f"{today:%m/%d/%Y}" # (as of writing this) 07/01/2024
print(todays_date)

"""Times"""
# Structure as follows
# variable = dt.time([hour,[minute,[second,[microsecond]]]])
midnight = dt.time() 
print(midnight) # 00:00:00
print(type(midnight)) # <class 'datetime.time'>
almost_midnight = dt.time(23, 59, 59, 999999)
print(almost_midnight) # 23:59:59:999999
# Time now
right_now = dt.datetime.now() # 2024-07-01 11:27:37.592748
print(right_now) 
new_years_eve = dt.datetime(2019, 12, 31, 23, 59) # 2019-12-31 23:59:00
print(new_years_eve)

"""Calculating Timespans"""
new_years_day = dt.date(2019, 1, 1)
memorial_day = dt.date(2019, 5, 27)
days_between = memorial_day - new_years_day # days_between is of class 'datetime.timedelta'
print(days_between) # 146 days, 0:00:00
# Deltas go as follows
# dt.timedelta(days=, seconds=, microseconds=, milliseconds=, hours=, days=, weeks=)
duration = dt.timedelta(days=146)
print(new_years_day + duration) # 2019-05-27
print(memorial_day - duration) # 2019-01-01
start_time = dt.datetime(2019, 3, 31, 8, 0, 0)
finish_time = dt.datetime(2019, 3, 31, 14, 34, 45)
time_between = finish_time - start_time
print(time_between) # 6:34:45
now = dt.datetime.now()
birthdatetime = dt.datetime(2008, 8, 16, 3, 42)
age = now - birthdatetime
print(age)
print(type(age))
birthdate = dt.date(2008, 8, 16)
delta_age = (today - birthdate)
print(delta_age)
days_old = delta_age.days
print(days_old, type(days_old))
years_old = days_old // 365 # floor division so no decimal part
print(f"You are {years_old} years old.") # USE THIS MORE ADAM

"""Timezones"""
# This is all broken
"""
# Get the time
here_now = dt.datetime.now()
# Get the UTC datetime right now
# utc_now = dt.datetime.utcnow() # THE BOOK LIED IT NO WORKEE
utc_now = dt.datetime.now(dt.UTC) # It's like this now
time_difference = utc_now - here_now
print(f"My time   : {here_now:%I:%M %p}") # My time   : 12:10 PM
print(f"UTC time  : {utc_now:%I:%M %p}")  # UTC time  : 4:10 PM
print(f"Difference: {time_difference}")   # Difference: 4:00:00
"""
# UTC time right now (NO BROKE PLEZ)
utc = dt.datetime.now(gettz("Etc/UTC"))
print(f"{utc:%A %D %I:%M %p %Z}") # Monday 07/01/24 4:28 PM UTC
# USA Eastern time
edt = dt.datetime.now(gettz("America/New_York"))
print(f"{edt:%A %D %I:%M %p %Z}") # Monday 07/01/24 12:28 PM EDT
# USA Central time
cdt = dt.datetime.now(gettz("America/Chicago"))
print(f"{cdt:%A %D %I:%M %p %Z}") # Monday 07/01/24 11:28 AM CDT
# USA Mountain time
mdt = dt.datetime.now(gettz("America/Boise"))
print(f"{mdt:%A %D %I:%M %p %Z}") # Monday 07/01/24 10:28 AM MDT

pdt = dt.datetime.now(gettz("America/Los_Angeles"))
print(f"{pdt:%A %D %I:%M %p %Z}") # Monday 07/01/24 09:28 AM PDT

# Today I guess
event = dt.datetime(2024, 7, 1, 12, 45, 00)
# Show local date and time"
print("Local: " + f"{event:%D %I:%M %p %Z}" + "\n")
event_eastern = event.astimezone(gettz("America/New_York"))
print(f"{event_eastern:%D %I:%M %p %Z}")
event_central = event.astimezone(gettz("America/Chicago"))
print(f"{event_central:%D %I:%M %p %Z}")
event_mountain = event.astimezone(gettz("America/Denver"))
print(f"{event_mountain:%D %I:%M %p %Z}")
event_pacific = event.astimezone(gettz("America/Los_Angeles"))
print(f"{event_pacific:%D %I:%M %p %Z}")
event_utc = event.astimezone(gettz("Etc/UTC"))
print(f"{event_utc:%D %I:%M %p %Z}" + "\n")
# Actual today
event = dt.datetime.now()
# Show local date and time"
print("Local: " + f"{event:%D %I:%M %p %Z}" + "\n")
event_eastern = event.astimezone(gettz("America/New_York"))
print(f"{event_eastern:%D %I:%M %p %Z}")
event_central = event.astimezone(gettz("America/Chicago"))
print(f"{event_central:%D %I:%M %p %Z}")
event_mountain = event.astimezone(gettz("America/Denver"))
print(f"{event_mountain:%D %I:%M %p %Z}")
event_pacific = event.astimezone(gettz("America/Los_Angeles"))
print(f"{event_pacific:%D %I:%M %p %Z}")
event_utc = event.astimezone(gettz("Etc/UTC"))
print(f"{event_utc:%D %I:%M %p %Z}")
"""FINALLY WE ARE DONE WITH THAT STUFFF!"""

"""
Operators, Comparisons, Loops, and Functions
Stuff I already know, but there are some things hiding that maybe I don't know!
"""
# == is equal to
# != is not equal to
# < less than
# > greater than
# <= less than or equal to
# >= greater than or equal to
# and both
# or either
# not flip it

"""If statements"""
if True:
    False

sun = "down"
if sun == "down":
    print("Good night!")
print("I am here")
sun = "up"
if sun == "up":
    print("Good night!")
print("I am here")

total = 100
sales_tax_rate = 0.065
taxable = True
if taxable:
    print(f"Subtotal : ${total:.2f}")
    sales_tax = total * sales_tax_rate
    print(f"Sales Tax: ${sales_tax:.2f}")
    total = total + sales_tax
print(f"Total    : ${total:.2f}")

# Time based
now = dt.datetime.now()
# Based on hour
if now.hour < 12:
    print("Good morning")
else:
    print("Good afternoon")
print("I hope you are doing well!")

# elif
light_colour = "yellow"
if light_colour == "green":
    print("Go")
elif light_colour == "red":
    print("Stop")
else:
    print("Proceed with caution")
print("This executes no matter what")

age = 31
if age < 21:
    beverage = "milk"
elif age >= 21 and age < 80:
    beverage = "BEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEER"
else:
    beverage = "prune juice"
print("Have a", beverage)

"""Looping with for"""
for i in range(1, 11):
    print(i)
print("All done")

for x in "snorkel":
    print(x)
print("Done")

my_word = "snorkel"
for x in my_word:
    print(x)
print("Done")

for x in ["The", "rain", "in", "spain"]:
    print(x)
print("Done")

# We can adjust the step size:
for i in range(8, 47, 5):
    print(i)

# We can also count backwards:
for i in range(10, 4 - 1, -1):
    print(i)
# Breaking
answers = ["A", "B", "C", "D"]
for answer in answers:
    if answer == "":
        print("Incomplete")
        break
    print(answer)
print("Loop is done")
answers = ["A", "B", "", "D"]
for answer in answers:
    if answer == "":
        print("Incomplete")
        break
    print(answer)
print("Loop is done")
answers = ["A", "B", "", "D"]
for answer in answers:
    if answer == "":
        print("Incomplete")
        continue
    print(answer)
print("Loop is done")

# Nesting
for outer in ["First", "Second", "Third"]:
    print(outer)
    for inner in range(3):
        print(inner + 1)
print("Both loops are done")

"""Looping with while"""
counter = 65
while counter < 91:
    print(counter, "=", chr(counter))
    counter += 1
print("all done")

counter = 0
while counter < 10:
    number = rnd.randint(1, 999)
    if number % 2 == 0:
        continue
    print(number)
    counter += 1
print("Loop is done")

"""Lists, Tuples and Sets"""
scores = [88, 92, 78, 90, 98, 84]
students = ["Mark", "Amber", "Todd", "Anita", "Sandy"]
print(students[0])
print(scores[4])
for score in scores:
    print(score)
has_anita = "Anita" in students
print(has_anita)
has_bob = "Bob" in students
print(has_bob)
print(len(students))
students.append("Goober")
new_student = "Amanda"
students.append(new_student)
print(students)

# Putting an item in a list
# Pos to insert it goes first
students.insert(0, "Lupe") 

# You can also overwrite a value
students[3] = "George"

# Extend combines lists
new_list = []
new_list.append(students)
new_list.extend(scores)
print(students)
print(new_list) # BROKEN WITH TWO EXTRA SQUARE BRACKETS, FUTURE ADAM PLEASE FIX
# Future me here, it is fixed at the bottom of all the list stuff! (ln 594)

# Remove removes an entry, not the specific spot
letters = ["A", "B", "C", "D", "C", "E", "C"]
# Only removes the first C
letters.remove("C") 
print("C")
while "C" in letters:
    letters.remove("C")
print(letters)

# Pop() is like del(), but can save the removed entry
letters = ["A", "B", "C", "D", "E", "F", "G"]
# Remove the first item
letters.pop(0) 
# Remove the last entry
letters.pop() 
# Display
print(letters)
letters = ["A", "B", "C", "D", "E", "F", "G"]
# Set first_removed to the first item and delete it
first_removed = letters.pop(0)
# Set last_removed to the last item and delete it
last_removed = letters.pop()
print(letters)
print(f"{first_removed} and {last_removed} were removed from the list")

# Delete does exactly what you think it does
letters = ["A", "B", "C", "D", "E", "F", "G"]
del letters[4]
print(letters)

# Clear clears it
letters.clear()
print(letters)

# Count, well, counts.
grades = ["C", "B", "A", "D", "C", "B", "C"]
# Set b_grades to how many "B"'s there are
b_grades = grades.count("B")
look_for = "C"
c_grades = grades.count(look_for)
print("There are", b_grades, "B grades in the list")
print("There are", c_grades, look_for, "grades in the list")
print("There are", grades.count("F"), "F grades in the list")

# Index finds the thing like wow
b_index = grades.index("B")
print(b_index)

# Python has a sort, but I wonder what sorting algorithm it uses . . .
# Did a bit of research, it uses 'Timsort'
names = ["Zara", "Lupe",  "Hong(kong)", "Alberto", "Jake", "Tyler"]
numbers = [14, 0, 56, -4, 99, 56, 11.23]
# Sort the names in alphabetic order
names.sort()
# Sort numbers from smallest to largest
numbers.sort()
print(names)
print(numbers)
# Can also do
numbers = [14, 0, 56, -4, 99, 56, 11.23]
numbers.sort(reverse=True)
print(numbers)
# Another way of getting that is, you guessed it
names.reverse()
print(names)
# So I had this problem with entagled lists, up in "Extend combines lists" (ln 523), this is the proper way to do it
new_list = students.copy()
new_list.extend(scores)
print(students)
print(new_list)

"""Tuples"""
# A tuple is an uneditable list
# Wait you would have to edit it tho to add new data to it . . .
new_tuple = ("e")

"""Sets"""
# A list where none of the items have an index
# HOW DO YOU FIND ANYTHING IN IT?
sample_set = {1.98, 98.9, 74.95, 2.5, 1, 16.3}
# Add one item to the set
sample_set.add(11.23)
# Add multiple items [remember the square brackets]
sample_set.update([88, 123.45, 2.98])
# This also means you can update it using a list
sample_set.update(scores)
print(sample_set)

"""
It is time for massive data storage. 
We are pulling out DICTIONARIES!
"""
people  = {
    'htanaka': 'Haru Tanaka',
    'ppatel': 'Priya Patel',
    'bagarcia': 'Benjamin Alberto Garcia',
    'zmin': 'Zhang Min',
    'afarooqi': 'Ayesha Farooqi',
    'hajackson': 'Hanna Jackson',
    'papatel': 'Pratyush Aarav Patel',
    'hrjackson': 'Henry Jackson'
}
print(people)

# Print the info stored under 'zmin'
print(people['zmin'])
person = "zmin"
print(people[person])
print(len(people))

# Use get to see if it exists
person = "bagarcia"
print(people.get(person))
# You can use a comma for a custom null message (displays None by default)
print(people.get("schmeedledorp", "Unbeknownst to this dictionary"))

# Overwrite a value
print(people['hajackson'])
people['hajackson'] = "I EAT PIGH"
print(people['hajackson'])

# Update can be used for adding a new item, and updating one
people.update({'gsbrown': 'George Brown'})
people.update({'hajackson': 'Hanna Jackson'})
print(people['hajackson'])
print(people['gsbrown'])
print(people)

# Print out the entire list like chunk bruv
for person in people:
    print(person, "=", people[person])
# I would like use a function for this but we haven't gotten to that in the book yet ☺░▒▓ (alt + 1, 176, 177, 178)
print("☺▓▒░▒▓☺")
for person in people:
    yes1 = str(person)
    yes2 = str(people[person])
    yes3 = ""
    yes4 = ""
    hest = 0
    for i in yes1:
        yes3 += "☺"
        yes3 += yes1[hest]
        hest += 1
    yes3 += "☺"
    hest = 0
    for i in yes2:
        yes4 += "☺"
        yes4 += yes2[hest]
        hest += 1
    yes4 += "☺"
    print(yes3, "=", yes4)

# To get only the keys (e.g. "ppatel", "bagarcia"), use the following:
for person in people:
    print(person)
# To get only the values (e.g. "Priya Patel", "Benjamin Alberto Garcia"), use the following:
for person in people:
    print(people[person])
# You can also use .values() to get only the values in a much better fashion
for person in people.values():
    print(person)
# .items() can also be used for cooler stuff, like double variables
for key, value in people.items():
    print(key, "=", value)

# Same as the list fiasco (ln 594), you can use .copy() to copy a dictionary
peeps2 = people.copy()
print(people)
print(peeps2)

# Wow I really wonder what del does hmmmmmmmmmmmmmmmmmmmmmmmmmmmm
del peeps2['zmin']
print(peeps2)
# You can also use del like variables to wipe them off the face of the earth and cause errors

# .clear() is used to erase the dictionary without deleting it
peeps2.clear()
print(peeps2)
peeps2 = people.copy()

# When using .pop(), it copies the value of that key to a variable while also deleting the entry
adios = peeps2.pop('zmin')
print(adios)
print(peeps2)

# .popitem() removes the last entry but copies both the key and value to the variable
adios = peeps2.popitem()
print(adios)
print(peeps2)

# You can have multiple data types in a dictionary
product = {
    'name': 'Ray-Ban Wayfarer Sunglasses',
    'unit_price': 112.99,
    'taxable': True,
    'in_stock': 10,
    'models': ["Black", "Tortoise"]
}
print(product['name'])
print(product['unit_price'])
print(product['taxable'])
print(product['in_stock'])
print(product['models'])
print("")
# Fancier
print("Name:    ", product['name'])
print("Price:   ", f"${product['unit_price']:.2f}")
print("Taxable: ", product['taxable'])
print("In Stock:", product['in_stock'])
print("Models:")
for model in product['models']:
    print(" " * 10 + model)

"""Using dict.fromkeys() and .setdefualt() newdictionaryname = dict.fromkeys(iterable[,value])"""
DWC001 = dict.fromkeys(['name', 'unit_price', 'taxable', 'in_stock', 'models'])
print(DWC001)

# Instead of doing all that, you can use .keys() to just get the keys from another dictionary
DWC001 = dict.fromkeys(product.keys())
print(DWC001)

# .setdefault() is like .update(), but it WILL NOT overwrite exiting keys, even if their value is undefined (none)
DWC001.setdefault('taxable', True)
DWC001.setdefault('models', [])
DWC001.setdefault('reorder_point', 100)
print(DWC001) # Everything stays at none, except reorder point is added with value of 100
DWC001['taxable'] = True
print(DWC001) # 'taxable' is now True

"""Nesting Dictionaries"""
# Create dictionary with multiple nested dictionaries
products = {
    'RB0011': {
        'name': 'Ray-Ban Sunglasses',
        'price': 112.98,
        'models': ["Black", "Tortoise"]
        },
    'DWC0317': {
        'name': 'Drone with Camera',
        'price': 72.95,
        'models': ["White", "Black"]
        },
    'MTS0540': {
        'name': 'T-Shirt',
        'price': 2.95,
        'models': ["Small", "Medium", "Large"]
        },
    'ECD2989': {
        'name': "Echo Dot",
        'price': 29.99,
        'models': []
    }
}
# Header
print("\n" * 3 + f"{'ID':<6} {' Name':<17} {'Price':>8} {' Models'}")
print("-" * 60) # Prints 60 hyphens
# Loop through each key
for oneproduct in products.keys():
    # The ID is the key
    id = oneproduct
    # Get the name
    name = products[oneproduct]['name']
    # Get unit price and format it
    unit_price = "$" + f"{products[oneproduct]['price']:,.2f}"
    # Create empty string
    models = ""
    for m in products[oneproduct]['models']:
        models += m + ", "
    # If the length of models is more than 2 characters, peel off the last comma and space
    if len(models) > 2:
        models = models[:-2]
    else:
        # If models is empty (just , ), set it to <none>
        models = "<none>"
    # More formatting yay print it
    print(f"{id:<6} {name:<17} {unit_price:>8} {models}")
print("")

"""
FUNCTIONS!!!
"""
def hello(user_name): # Practice Function
    """Docstring describing the function \n
    Shows up when you hover over the function \n
    Only works in VS Code"""
    # The \n is for formatting in the text box
    print("Hello", user_name)
hello("Alan")
this_person = "Alan"
hello(this_person)

# You can add defaults
def hello(user_name = "nobody"):
    print("Hello", user_name)
hello("Alan")
hello()

# Some useful stuff
def hello(fname, lname, datestring):
    print("Hello", fname.capitalize(), lname.capitalize())
    print("The date is", datestring)
hello("Alan", "Simpson", "12/31/2019")

# You can make params optional with defaults
def hello(fname, lname, datestring = ""):
    msg = "Hello " + fname.capitalize() + " " + lname.capitalize() # Annoying that I have to do this to avoid tuples
    if len(datestring) > 0:
        msg += ", you mentioned " + datestring
    print(msg)
hello("Alan", "Simpson", "12/31/2019")
hello("Sammy", "Schmeedledorp")

# You can use keyword arguments, instead of the function just assuming
hello(datestring = "13/31/2019", lname = "Simpson", fname = "Alan")
appt_date = "12/31/2019"
last_name = "Janda"
first_name = "Kylie"
hello(datestring = appt_date, lname = last_name, fname = first_name)

# Pass in any number of args, stored as a tuple
def sorter(*args):
    # Convert to list and copy
    newlist = list(args)
    newlist.sort()
    print(newlist)
sorter(1, 0.001, 100000, -900, 2)

# Returning values
def alphabetize(original_list = []):
    """Pass any list in square brackets, \n
    Displays a string with items sorted."""
    # Make a copy of the list
    sorted_list = original_list.copy()
    # Just sort the damn thing
    sorted_list.sort()
    # String time
    final_list = ""
    for name in sorted_list:
        final_list += name + ", "
    final_list = final_list[:-2]
    # Return it 
    return final_list
random_list = ["McMullen", "Keaser", "Maier", "Wilson", "Yudt", "Gallagher", "Jacobs", "Schrepfer", "Maier", "Santiago", "Adams"]
alpha_list = alphabetize(random_list)
print(alpha_list)

"""Anonymous Functions (Lambda)"""
names = ["Adams", "Ma", "diMeola", "Zandusky"]
names.sort()
print(names) # diMeola comes after Zandusky, (because of lowercase,) which just looks wrong

# We can fix it using a function as the key
def lowercaseof(anystring):
    return anystring.lower()
names = ["Adams", "Ma", "diMeola", "Zandusky"]
# The key applies to all items, and then sorts them
# In this case it makes everything lowercase and then sorts it
names.sort(key = lowercaseof)

# We can also use lambda expressions
names = ["Adams", "Ma", "diMeola", "Zandusky"]
names.sort(key = lambda s: s.lower()) # Note the "s" can be any string. It just defines the string and mandates what happens to it
print(names)

# lambda functions do not require def to define them
currency = lambda n: f"${n:,.2f}"
percent = lambda n: f"{n:.2%}"

print(currency(99))
print(currency(123456789.09876543))

print(percent(0.065))
print(percent(.5))

# You can define the functions normally
def currency(n):
    return f"${n:,.2f}"
def percent(n):
    return f"{n:.2%}"

# And do some crazy stuff
def currency(n, w = 15):
    s = f"${n:,.2f}"
    return s.rjust(w)
def percent(n, w = 15):
    s = f"{n:.2%}"
    return s.rjust(w)

print(currency(9999))
print(currency(9999, 20))


print("""
YO WASSUP THE BIG BOI IS IN TOWN
THE THIK HEAD HURTY SECTION IS AHEAD
IT'S TIME FOOORRRR
((((( [     {{{{{ ||||| }}}}} ]]]]] )))))
(     [     {   { |     }     ]     )
(     [     {{{{{ ||||| }}}}} ]]]   )))))
(     [     {   {     |     } ]         )
((((( [[[[[ {   { ||||| }}}}} ]]]]] )))))
"""
)

# Define new class, Member
class Member:
    pass # Stops python from throwing errors because the class is incomplete

# To create instances of itself, use the __init__ method
# def __init__(self, suppliedprop1, suppliedprop2, ...)
# def defines it
# __init__ is the method that creates objects in a class
# self is just the variable that the object refers to (you can use other words but self is explanitory)
# you can use ": type" to lock a varible input to a class
# username: str, yesno: bool

# To create methods to execute for an instance, use functions
# def methodname(self, param1, param2, ...)

# You can alse create a value that applies to all instances as they are created, using variables
# variablename = value

# Class methods also exist, to operate on the entire class, and are defined using the class method
# @classmethod
# def methodname(cls, x, ...)
# @classmethod makes it a class method
# def defines it
# methodname is just the name of the method
# cls is just the variable that the class method refers to (you can use other words but cls is explanitory)

class Member:

    free_days = 90

    def __init__(self, username: str, fullname: str): # Data you pass in to create the object
        # Set attributes to those variables
        self.username = username
        self.fullname = fullname
        self.date_joined = dt.date.today()
        self.is_active = True
        self.free_expires = dt.date.today() + dt.timedelta(days = Member.free_days)
    
    def show_datejoined(self):
        return f"{self.fullname} joined on {self.date_joined:%m/%d/%y}"
    
    def activate(self, yesno: bool):
        self.is_active = yesno

    @classmethod
    def setfreedays(cls, days):
        cls.free_days = days
    
    @staticmethod
    def currenttime():
        now = dt.datetime.now()
        return f"{now:%I:%M %p}"

    
    
    


"""Instance from a class"""
# You can make an instace by crating a variable from that class, and do the class operations on it

# Create instance called "new_guy"
new_guy = Member("Rambo", "Rocco Moe")

# See the instance and its properties
print(new_guy)
print(new_guy.username)
print(new_guy.fullname)
print(type(new_guy))

# Change attribute value
new_guy.username = "Princess"
print(new_guy.username)

print(new_guy.is_active)
new_guy.activate(False)
print(new_guy.is_active)

# You can also access values using the class
wilbur = Member("wblomgren", "Wilbur Blomgren")

print(wilbur.show_datejoined())
print(Member.show_datejoined(wilbur))

print(wilbur.free_expires)

Member.free_days = 90

print(Member.currenttime)

"""Subclass stuff"""
# Generic class
# Subclasses are of structure: class subclassname(mainclassname): e.g; class Admin(Member):
class Member:
    expiry_days = 365

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.expiry_date =dt.date.today() + dt.timedelta(days = self.expiry_days)
        # Default secret code is nothing
        self.secretcode = ""
    
    # Internal functions
    def showexpiry(self):
        return f"{self.firstname} {self.lastname} expires on {self.expiry_date}"
    
    def get_status(self):
        return f"{self.firstname} is a Member"

class Admin(Member):
    expiry_days = 365.2422 * 100 # Can overwrite main class vars
    
    # Needs to have the same stuff at least as the main class
    # Any parameters that belong to the __init__ main class must be passed up using super().__init__(param1, param2)
    def __init__(self, firstname, lastname, secret_code): 
        super().__init__(firstname, lastname)
        self.secretcode = secret_code
    
    def get_status(self):
        return f"{self.firstname} is an Admin"

class User(Member):
    def get_status(self):
        return f"{self.firstname} is a User"


Joe = Member("Joe", "Anybody")
print(Joe.firstname)
print(Joe.lastname)
print(Joe.expiry_date)

# Admin and User are created normally
Ann = Admin("Annie", "Angst", "PRESTO")
print(Ann.firstname, Ann.lastname, Ann.expiry_date, Ann.secretcode)


Uli = User("Uli", "Ungula")
print(Uli.firstname, Uli.lastname, Uli.expiry_date)

print(Ann.showexpiry())
print(Uli.showexpiry())

print(Ann.get_status())
print(Uli.get_status())
print(Joe.get_status())

print(Admin.__dict__)

"""Error handling"""
# try, except Exception
# ValueError
# FileNotFoundError
# AttributeError
# except is to stroe the error also
# else I guess does stuff if like uhh (why not just let the rest of the code run?)
# finally executes no matter what happens
try:
    thefile = open("people.csv")
    leg = 42 + "e"
except FileNotFoundError:
    print("Yeah nothing")
except Exception as e: # only if there is another error than previous excepts
    print(e)
else:
    print("What")
finally:
    print("Yeah this is here")


"""
Working With External Files!!
"""
# open(filename.ext[,mode])
# open("example.txt", "a")
# mode is optional, the default is Read
# if the file is not in same folder, you must provide the full file path (STAY TUNED IF I CAN FIX THE NOT C: ISSUE)
# b ("binary") is used for binary media (everything other than a text file) slap it right next to the mode ("rb")
# use forward slashes (Linux already does), /media/sammy/OS/Users/adamt/Documents/Personal Python Folders/Misc
'''Mode:   Name:                   Desc:                          Creates file:       Throws error if:'''
#  r       Read         Does not allow any changes                     No            File does not exist
#  r+    Read/Write          Allows full changes                       No            File does not exist
#  a      Append       Only allowed to add new stuff                   Yes                 Cannot
#  w      Write              Allows full changes                       Yes                 Cannot
#  x      Create                Creates file                           Yes           File already exists

# you can assign the file to a variable, f is commonly used
f = open("Education/hello.py")
# .read() dumps all the contents
filecontents = f.read()
# make sure to close, to not like break stuff and that
f.close()
# .closed checks if it is closed
print(f.closed)

# with open automatically closes the file 
with open("/home/sammy/Downloads/Alex.webp", "rb") as f:
    filecontents = f.read()
    # print(filecontents) Don't cause it's a massive wall of garbage

"""Reading Contents"""
# read([size]) empty parentheses read the entire file, a number specifies the number of characters, or bytes to read
# readline() reads one line, the line ends at a newline character (\n)
# readlines() reads all of the lines of a text file into a list
# read() is one chunk of data, readlines() stores each line as an entry in the list
with open("Education/quotes.txt") as f:
    content = f.readlines()
    print(content)
with open("Education/quotes.txt") as f:
    content = f.readline()
    print(content)

# looping with readlines()
with open("Education/quotes.txt") as f:
    # Reads in all lines first, then loops through
    for one_line in f.readlines():
        print(one_line, end='')

# more complicated stuff
with open("Education/quotes.txt") as f:
    # Reads in all lines first, then loops through
    # Count each line starting at zero
    for one_line in enumerate(f.readlines()):
        # enumerate crash course:
        # one_line[0] contains the line number
        # one_line[1] contains the contents
        # If counter is even number, print with no extra newline (remember starting from 0)
        if one_line[0] % 2 == 0:
            print(one_line[1], end='')
        # Otherwise print a couple spaces and an extra newline
        else:
            print('  ' + one_line[1])

# looping with readline(), to save RAM
with open("Education/quotes.txt") as f:
    one_line = f.readline()
    while one_line: # loop as long as one_line isn't empty
        print(one_line, end='')
        one_line = f.readline()
