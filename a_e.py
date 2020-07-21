#Write code that counts the number of words in sentence that contain either an “a” or an “e”.
#Store the result in the variable num_a_or_e.
#below is the variable "sentence" containing the input
sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
#variable to Store the result
num_a_or_e=0
#split each words in the sentence
words=sentence.split()

#for every word in the words list ,check whether it contains a or e
for i in words:
    if ("a" in i)or("e" in i):
        num_a_or_e=num_a_or_e+1
