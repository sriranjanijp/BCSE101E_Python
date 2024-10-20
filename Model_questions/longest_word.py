#Find the longest word in a sentence
sentence = 'Hongjoong - Did i teach you to dream small?'
length = count = 0
word = big = ''
for i in range(0,len(sentence)):
    if sentence[i]!=' ':
        count += 1
        word += sentence[i]
    else:
        count = 0
        word = ''
    if len(word)>length:
        big = word
        length = count  
print(big)
