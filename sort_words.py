
#python program to read a file and then read every lines , store evry words in a list
# sort the list alphabetically 


fname = input("Enter file name: ")
fh = open(fname)
lst = list()
wordlist=[]
for line in fh: 
    words=line.split()
    for x in words:
        if x not in wordlist:
    	   wordlist.append(x)

x=sorted(wordlist)
print(x)
