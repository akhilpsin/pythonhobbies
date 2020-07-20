#Write code that counts the number of words in sentence that contain either an “a” or an “e”.
#Store the result in the variable num_a_or_e.
sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
num_a_or_e=0
words=sentence.split()
for i in words:
    if ("a" in i)or("e" in i):
        num_a_or_e=num_a_or_e+1
