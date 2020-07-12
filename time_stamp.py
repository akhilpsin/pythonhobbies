#Write a program to read through the mbox-short.txt and figure out the 
#distribution by hour of the day for each of the messages. You can pull the hour
#out from the 'From ' line by finding the time and then splitting the string a
#second time using a colon. 

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
time={}
for lines in handle:
    if lines.startswith("From "):
        words=lines.split()
        time_stamp=words[5].split(":")
        if time_stamp[0] not in time:
            time.update({time_stamp[0]:1})
        else :
            time[time_stamp[0]]=time.get(time_stamp[0],0)+1
        
sorteddict = sorted(time)
for index in sorteddict :
    print(index , time[index])
        
