




fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
existing=[]
for line in fh:
    if line.startswith("From "):
        words=line.split()
        #if words[1] not in existing:
        print(words[1])
        existing.append(words[1])
        count=count+1

print("There were", count, "lines in the file with From as the first word")
