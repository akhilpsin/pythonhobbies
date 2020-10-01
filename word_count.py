#function for counting each word is created
def word_count(str):
    counts = dict()
    words = str.split() #here each letters is splited 

    for word in words: #here in this 'for loop' until the words are over this loop continues
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('the quick brown fox jumps over the lazy dog.'))
