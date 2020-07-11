# Write a program that prompts for a file name, then opens that file and reads through the file, 
# looking for lines of the form: 
# X-DSPAM-Confidence:    0.8475

##Count these lines and extract the floating point values from each of the lines 
#and compute the average of those values and produce an output as shown below. 
#Do not use the sum() function or a variable named sum in your solution. 

fname = input("Enter file name: ")
fh = open(fname)
avg_sm=0.0
line_count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    index=line.find(":")
    number=float(line[index+1:])
    avg_sm=avg_sm+number
    line_count=line_count+1
line_count=float(line_count)
average= avg_sm/line_count
print("Average spam confidence:" ,average)

