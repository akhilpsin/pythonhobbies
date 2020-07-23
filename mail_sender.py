#Write a program to read through the mbox-short.txt and figure out
#who has sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of those lines as
#the person who sent the mail. The program creates a Python dictionary that maps
#the sender's mail address to a count of the number of times they appear in the file.
#After the dictionary is produced, the program reads through the dictionary using
#a maximum loop to find the most prolific committer.

#get the file name
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
#open the file
handle = open(name)
user={}
for lines in handle:
    if lines.startswith("From "):
        words=lines.split()
        if words[1] not in user :
            user.update({words[1]:1})
        else :
            user[words[1]]=user.get(words[1],0)+1
maximum=0
maximum_key=0
for i in user :
    if user[i]>maximum:
        maximum=user[i]
        maximum_key=i

print(maximum_key ,user[maximum_key])
