# Write a program that prompts for a file name, then opens that file and reads through the file,
# and print the contents of the file in upper case.
#we need to get the file name
fname = input("Enter file name: ")

#open the file using open function
fh = open(fname)
y=fh.read()
y=y.strip()
print(y.upper())
