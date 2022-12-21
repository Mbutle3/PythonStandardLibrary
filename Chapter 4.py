# Datetime Module Part I
import calendar
from datetime import datetime

now = datetime.now()
print(now.date())
print(now.year)
print(now.month)
print(now.hour)  # military time
print(now.minute)
print(now.second)
print(now.time())  # hr:ms:s.ms
# Getting more control over formatting
"""
Formatting Dates and Times: Days
    %a -> abbreviated day of week: Mon, Tues, Wed
    %A -> full day of week: Monday, Tuesday, Wednesday
    %d -> day of month: number 10 for the 10th of January
"""
print(now.strftime('%a %A %d'))  # abb full num
"""
Formatting Dates and Times: Months
    %b -> abbreviated month name: Jan, Feb
    %B -> full month name: January
    %m -> month as number: 01 or January
"""
print(now.strftime('%b %B %m'))  # abb full num
# day abb, full month name, day of month as number
print(now.strftime('%a %B %d'))
"""
Formatting Dates and Times: Times
    %H -> hours
    %M -> minutes
    %S -> seconds
    %p -> a.m or p.m
"""
print(now.strftime('%H : %M : %S %p'))
"""
Formatting Dates and Times: Years
    %y -> abbreviated year as two numbers: 17
    %Y -> year as four numbers: 2014
"""
print(now.strftime('%y %Y'))

# Calendar Module
from datetime import datetime, timedelta

# timedelta - used to get information about future and past times
now = datetime.now()
testDate = now + timedelta(days=2)  # upcoming test in 2 days
print(testDate.date())
myFirstLinkedInCourse = now - timedelta(weeks=4)  # started a month ago
print(myFirstLinkedInCourse)
if testDate > myFirstLinkedInCourse:
    print("Comparison works")
cal = calendar.month(1999, 8)
print(cal)
cal2 = calendar.weekday(1999, 8, 14)  # what the week day of (aug 14 1999)?
print(cal2)  # returned 5 which is Saturday
print(calendar.isleap(1999))  # check if it's a leap year
print(calendar.isleap(2000))

# Create a Timer with the Time module

import time

"""
run = input("Start? > type yes\n")
seconds = 0
if run == 'yes':
    # while seconds != 10:
    while seconds != 0:
        print('>', seconds)
        time.sleep(1)
        seconds += 1
    print(">", seconds)
    print("10 seconds have passed")
"""

# HTML Parser Module
"""
    <p> -> opening paragraph tag
    </p> -> closing paragraph tag
    <!-- important notes --> -> comment
    <h1> Hello World </h1> -> an H1 header with the data "Hello World"
"""
from html.parser import HTMLParser


class HTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag: ", tag)
        for attr in attrs:
            print("attr: ", attr)

    def handle_endtag(self, tag):
        print("End tag: ", tag)

    def handle_comment(self, data):
        print("Comment: ", data)

    def handle_data(self, data):
        if data == '\n':
            return
        print("Data: ", data)


parser = HTMLParser()
parser.feed("<html><head><title>Coder</title></head><body><h1><!--hello-->I am a coder</h1></body></html>")
print()
# input = input("Put in HTML Code\n")
# parser.feed(input)
print()
htmlFile = open("sample.html", "r")
s = ""
for line in htmlFile:
    s += line
parser.feed(s)

# Text Wrap Module
import textwrap

websiteText = """Learning can happen anywhere with our apps on your computer and mobile devices. Limitless learning, 
Limitless possibilities, Limitless potential"""

print("\nNo Dedent: ")
print(textwrap.fill(websiteText))


print("Dedent: ")
dedent_text = textwrap.dedent(websiteText).strip()
print(dedent_text)

print("Fill")
print()
print(textwrap.fill(dedent_text, width=50))
print("Controlling Indent")
print(textwrap.fill(dedent_text, initial_indent="   ")) # 3 spaces indent
print("Subsequent Indent")
print(textwrap.fill(dedent_text, initial_indent="   ", subsequent_indent="          ")) # 3 spaces indent
print("Shortening Text")
shorten = textwrap.shorten("LinkedIn.com is great!", width=15, placeholder="...")
print(shorten)