# # Input/Output Module
print('Hello World')
color = input("Enter Your Favorite Color\n")
print(f"My favorite color is {color} too!")
# Files and File Writing Modules
# Open a file
# w --> write
# r --> read
# r+ --> read and write
# a --> append
myFile = open("DBZPowerLevels.txt", "r")
print("Name: " + myFile.name)
print("Mode: " + myFile.mode)
# Write to the file
myFile = open("DBZPowerLevels.txt", "w")
myFile.write('Goku : 9001\n'
             'Vegeta : 8400\n'
             'Chiaotzu : 15000')
myFile.close()
# Read the file
myFile = open("DBZPowerLevels.txt", "r")
print(f"Reading Power Levels: {myFile.read(11)}")
print(f"Reading Power Levels Again: {myFile.read(12)}")  # didn't reset seek pointer or close the file
# Seek = A pointer that keeps track of where we are in a file
#        Before reading or writing to a file, seek must be set back to zero
myFile.seek(0)
print(f"Reading Power Levels A Third Time: {myFile.read(12)}")  # didn't reset seek pointer or close the file
# Iterative Files
myFile = open("DBZPowerLevels.txt", "r")
# read only one line at a time
print("my one line: " + myFile.readline())
myFile.seek(0)
# iterate through each line of a file
for line in myFile:
    newPowerLevel = line.replace("Chiaotzu", "Gohan")  # (Does Not Save In File Since We Are Only Reading)
    print(newPowerLevel)
myFile.close()
# Best to create a new file instead of appending a file


# Tempfile Module
import tempfile

# Create a temporary file
tempFile = tempfile.TemporaryFile()
# Write to a temporary file
tempFile.write(b'Save this special number for me: 123456')  # b turns this into a byte literal object instead of a str
tempFile.seek(0)
# Read the temporary file
print(tempFile.read())
# close the temporary file
tempFile.close()

# Zipfile Module
import zipfile

# Open and List
zip = zipfile.ZipFile('Archive.zip', 'r')
print(zip.namelist())
print('---')
# Metadata in the zip folder
for meta in zip.infolist():
    print(meta)
print('---')
# Access to files in zip folder
print("'Purchased' : " + str(zip.read('purchases.txt')))
print(" Wish list: A " + str(zip.read('wishlist.txt')))
print('---')
with zip.open('purchases.txt') as f:
    print(f.read())
# Extracting files
zip.extract('purchases.txt')
zip.extractall()
# Closing the zip
zip.close()

# very helpful if you are working with zip files in projects

